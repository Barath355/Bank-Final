from flask import Blueprint, request, jsonify
from backend.extensions.db import db
from backend.models.account_model import Account
import random

account_bp = Blueprint("account", __name__)

# ✅ Create Account
@account_bp.route("/create", methods=["POST"])
def create_account():
    data = request.json

    account_number = str(random.randint(1000000000, 9999999999))

    new_account = Account(
        user_id=data["user_id"],
        account_number=account_number,
        balance=0.0
    )

    db.session.add(new_account)
    db.session.commit()

    return jsonify({
        "message": "Account created",
        "account_number": account_number
    })


# ✅ Get Account Details
@account_bp.route("/<account_number>", methods=["GET"])
def get_account(account_number):
    account = Account.query.filter_by(account_number=account_number).first()

    if not account:
        return jsonify({"error": "Account not found"}), 404

    return jsonify({
        "account_number": account.account_number,
        "balance": account.balance
    })


# ✅ Check Balance
@account_bp.route("/balance/<account_number>", methods=["GET"])
def check_balance(account_number):
    account = Account.query.filter_by(account_number=account_number).first()

    if not account:
        return jsonify({"error": "Account not found"}), 404

    return jsonify({
        "balance": account.balance
    })