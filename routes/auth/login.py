from flask import Blueprint, request, jsonify
from services.auth.login import verifyLogin

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"message": "invalid input"}), 400
    try:
        result = verifyLogin(data['email'], data['password'])
        return jsonify({"response": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
