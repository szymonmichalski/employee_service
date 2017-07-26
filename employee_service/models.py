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
    #
    # def __repr__(self):
    #     return '<Employee %r>' % self.follower_follower_name
