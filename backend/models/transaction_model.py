from backend.extensions.db import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    from_account_id = db.Column(db.Integer, nullable=True)
    to_account_id = db.Column(db.Integer, nullable=True)

    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20))  # deposit, withdraw, transfer

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    