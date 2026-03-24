from flask import Blueprint, request, jsonify
from backend.extensions.db import db
from backend.models.account_model import Account
from backend.models.transaction_model import Transaction

transaction_bp = Blueprint("transactions", __name__)

#---------------#Deposit----------------#
@transaction_bp.route("/deposit", methods=["POST"])
def deposit():
    data = request.json

    acc_num = data["account_number"]
    amount = data["amount"]

    account = Account.query.filter_by(account_number=acc_num).first()

    if not account:
        return jsonify({"message": "Account not found"}), 404

    account.balance += amount

    txn = Transaction(
        to_account_id=account.account_number,
        amount=amount,
        type="deposit"
    )

    db.session.add(txn)
    db.session.commit()

    return jsonify({
        "message": "Deposit successful",
        "balance": account.balance
    })

#---------------#Withdraw----------------#
@transaction_bp.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.json

    acc_num = data["account_number"]
    amount = data["amount"]

    account = Account.query.filter_by(account_number=acc_num).first()

    if not account:
        return jsonify({"message": "Account not found"}), 404

    if account.balance < amount:
        return jsonify({"message": "Insufficient balance"}), 400

    account.balance -= amount

    txn = Transaction(
        from_account_id=account.account_number,
        amount=amount,
        type="withdraw"
    )

    db.session.add(txn)
    db.session.commit()

    return jsonify({
        "message": "Withdraw successful",
        "balance": account.balance
    })

#---------------#Transfer----------------#

@transaction_bp.route("/transfer", methods=["POST"])
def transfer():
    data = request.json

    from_acc_num = data["from_account_number"]
    to_acc_num = data["to_account_number"]
    amount = data["amount"]

    from_acc = Account.query.filter_by(account_number=from_acc_num).first()
    to_acc = Account.query.filter_by(account_number=to_acc_num).first()

    if not from_acc:
        return jsonify({"message": "Sender account not found"}), 404

    if not to_acc:
        return jsonify({"message": "Receiver account not found"}), 404

    if from_acc.balance < amount:
        return jsonify({"message": "Insufficient balance"}), 400

    # 💰 Transfer logic
    from_acc.balance -= amount
    to_acc.balance += amount

    txn = Transaction(
        from_account_id=from_acc.account_number,
        to_account_id=to_acc.account_number,
        amount=amount,
        type="transfer"
    )

    db.session.add(txn)
    db.session.commit()

    return jsonify({
        "message": "Transfer successful",
        "from_account_balance": from_acc.balance,
        "to_account_balance": to_acc.balance
    })