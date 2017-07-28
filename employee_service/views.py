from flask import (
    render_template,
    request,
)

from employee_service.utils import EmployeeHandler
from employee_service.application import (
    app,
)


@app.route('/')
def homepage():
    return render_template(
        'homepage.html',
    )


@app.route('/employee', methods=['GET', 'POST', 'DELETE'])
def employee():
    employee_id = request.args.get('id')
    name = request.args.get('name')
    surname = request.args.get('surname')
    email = request.args.get('email')
    employee_handler = EmployeeHandler()
    if request.method == 'DELETE':
        return employee_handler.delete_employee(
            employee_id, name, surname, email)
    elif request.method == 'POST':
        return employee_handler.add_employee(name, surname, email)
    else:
        return employee_handler.get_employees(email)
