import json

import logging
from flask import (
    render_template,
    request,
    redirect,
    session,
)

from employee_service.utils import get_employees
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
    id = request.args.get('id')
    name = request.args.get('name')
    surname = request.args.get('surname')
    email = request.args.get('email')
    if request.method == 'DELETE':
        pass
    elif request.method == 'POST':
        pass
    else:
        return json.dumps(
            {
                'employees': get_employees(email)
            }
        )
