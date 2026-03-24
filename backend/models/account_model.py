from backend.extensions.db import db

class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    account_number = db.Column(db.String(20), unique=True)
    balance = db.Column(db.Float, default=0.0)