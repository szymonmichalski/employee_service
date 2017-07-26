from employee_service.application import db


def get_employees(email):
    from employee_service.models import \
        Employee
    if email:
        employees = list(
            db.session.query(Employee).filter_by(email=email))
    else:
        employees = list(
            db.session.query(Employee).all())
    return employees
