from flask import Blueprint, request, jsonify
from ..controllers.wallet_controller import WalletController

wallet_bp = Blueprint('wallet_routes', __name__)
controller = WalletController()

@wallet_bp.route('/', methods=['GET'])
def get_wallets():
    data = controller.get_all_wallets()
    return jsonify(data)

@wallet_bp.route('/<wallet_id>', methods=['GET'])
def get_wallet(wallet_id):
    data = controller.get_wallet(wallet_id)
    return jsonify(data)

@wallet_bp.route('/', methods=['POST'])
def create_wallet():
    wallet_data = request.get_json()
    data = controller.create_wallet(wallet_data)
    return jsonify(data), 201

@wallet_bp.route('/<wallet_id>', methods=['PUT'])
def update_wallet(wallet_id):
    wallet_data = request.get_json()
    data = controller.update_wallet(wallet_id, wallet_data)
    return jsonify(data)