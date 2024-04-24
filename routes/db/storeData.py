from flask import Blueprint, request, jsonify, current_app
from extensions.mysql import mysql

bp = Blueprint('storeData', __name__, url_prefix='/storeData')

@bp.route('/', methods=['POST'])
def storeData():
    data = request.get_json()
    referencedText = data['referenceText']
    generatedText = data['generatedText']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO trainingData(referenceText, generatedText) VALUES (%s, %s)", (referencedText, generatedText))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Data inserted successfully'}), 200