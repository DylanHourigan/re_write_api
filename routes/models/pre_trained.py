from flask import Blueprint, request, jsonify
from services.models.pre_trained import paraphrase

bp = Blueprint('paraphraseV2', __name__, url_prefix='/V2/paraphrase')

@bp.route('/', methods=['POST'])
def paraphraseV2():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400
    try:
        result = paraphrase(data['input'])
        return jsonify({"paraphrase": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
