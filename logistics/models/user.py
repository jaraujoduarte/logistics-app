from logistics import db
from logistics.models.base import BaseModel

class User(db.Model, BaseModel):
    """User model"""

    __tablename__ = "users"

    phone_number = db.Column(db.String(20), index=True, nullable=True)
    email = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=True)


    def __repr__(self):
        return "{firstname} - {lastname} - {email}".format(firstname=self.firstname, lastname=self.lastname,
                                                           email=self.email)