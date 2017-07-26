from flask import (
    render_template,
    request,
    redirect,
    session,
)

from employee_service.common import get_employees
from employee_service.application import (
    app,
)


@app.route('/')
def homepage():
    return render_template(
        'homepage.html',
    )


@app.route('/employee', methods=['GET', 'POST', 'DELETE'])
def employee(id = None, name=None, surname=None, email=None):
    if request.method == 'DELETE':
        pass
    elif request.method == 'POST':
        pass
    else:
        employees = get_employees(email)
        return render_template(
            'employees.html',
            employees=employees,
        )
