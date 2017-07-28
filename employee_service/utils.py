import json
from http import HTTPStatus

from sqlalchemy.exc import IntegrityError
from validate_email import validate_email

from employee_service.application import db
from employee_service.models import Employee
from sqlalchemy.orm.exc import NoResultFound


class EmployeeHandler:

    def get_employees(self, email):
        if email:
            employees = list(
                db.session.query(Employee).filter_by(email=email))
        else:
            employees = list(
                db.session.query(Employee).all())
        employees = [item.serialize for item in employees]
        return (
            json.dumps(
                {
                    'employees': employees
                }
            ),
            HTTPStatus.OK,
        )

    def delete_employee(self, employee_id, name, surname, email):
        if employee_id or name and surname and email:
            try:
                employee = self.find_one_employee(
                    employee_id, name, surname, email)
            except NoResultFound:
                return (
                    'Error: no such employee in the database.',
                    HTTPStatus.NOT_FOUND,
                )
        else:
            return (
                'Error: not enough parameters.',
                HTTPStatus.BAD_REQUEST,
            )
        try:
            employee_id = employee.id
            name = employee.name
            surname = employee.surname
            email = employee.email

            db.session.delete(employee)
            db.session.commit()
            return (
                'Employee {} {} with email {} and id {} deleted.'.format(
                    name, surname, email, employee_id),
                HTTPStatus.OK,
            )
        except Exception:
            return (
                'Employee was not deleted.',
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )

    def find_one_employee(self, employee_id, name, surname, email):
        try:
            if employee_id:
                return db.session.query(Employee).filter_by(
                    id=employee_id).one()
            elif name and surname and email:
                return db.session.query(Employee).filter_by(
                    name=name, surname=surname, email=email).one()
        except NoResultFound:
            raise NoResultFound

    def add_employee(self, name, surname, email):
        if name and surname and email:
            try:
                self.validate_email(email)
                self.add_employee_to_db(name, surname, email)
                return (
                    'Employee {} {} with mail {} was added.'.format(
                        name, surname, email),
                    HTTPStatus.CREATED,
                )
            except ValueError:
                return (
                    'Error: email is not correct.',
                    HTTPStatus.BAD_REQUEST,
                )
            except IntegrityError:
                return (
                    'Error: such email already exists in the database.',
                    HTTPStatus.CONFLICT,
                )
            except Exception:
                return (
                    'Error: Employee {} {} with mail {} was not added.'.format(
                        name, surname, email),
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                )
        else:
            return (
                'Error: Employee not added due to missing arguments.',
                HTTPStatus.BAD_REQUEST,
            )

    def add_employee_to_db(self, name, surname, email):
        employee = Employee(name, surname, email)
        db.session.add(employee)
        db.session.commit()

    def validate_email(self, email):
        is_valid = validate_email(email)
        if not is_valid:
            raise ValueError
