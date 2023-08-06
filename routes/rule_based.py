from flask import Blueprint, request, jsonify
from services.rule_based import paraphrase

bp = Blueprint('paraphrase', __name__, url_prefix='/V1/paraphrase')

@bp.route('/', methods=['POST'])
def paraphraseV1():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400
    try:
        result = paraphrase(data['input'])
        return jsonify({"paraphrase": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
