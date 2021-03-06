from application import db
from dataclasses import dataclass
from flask_login import UserMixin


@dataclass
class Customer(UserMixin, db.Model):
    id: int
    first_name: str
    last_name: str
    email: str
    pass_word: str
    phone_number: str
    home_address_id: int
    billing_address_id: int
    user_role: str

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(35), nullable=False)
    pass_word = db.Column(db.String(12), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    home_address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=False)
    billing_address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=False)
    user_role = db.Column(db.String(15), nullable=True)

