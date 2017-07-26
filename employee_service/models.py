from employee_service.application import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    surname = db.Column(db.String(100), unique=False)
    email = db.Column(db.String(100), unique=True)

    def __init__(
            self,
            name,
            surname,
            email,
    ):
        self.name = name
        self.surname = surname
        self.email = email

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
        }
