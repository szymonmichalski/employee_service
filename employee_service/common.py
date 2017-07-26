from employee_service.application import db


def get_employees(email):
    from employee_service.models import \
        Employee
    employees = list(
        db.session.query(Employee).filter_by(email=email))
    return employees
