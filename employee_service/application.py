from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from employee_service.config import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_POOL_RECYCLE'] = SQLALCHEMY_POOL_RECYCLE
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy(app)

import employee_service.views

if __name__ == '__main__':
    app.run()
