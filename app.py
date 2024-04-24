import os
from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from extensions.mysql import mysql
from routes.models.rule_based import bp as rule_based_bp
from routes.models.pre_trained import bp as pretrained_bp
from routes.db.storeData import bp as store_data_bp

Flask.debug = True

mysql = MySQL()
def create_app():
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:8080', 'https://dylanhourigan.github.io'])

    mysql.init_app(app)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'rewrite'
    app.config['MYSQL_PASSWORD'] = 'pass'
    app.config['MYSQL_DB'] = 'rewrite'
    
    app.register_blueprint(rule_based_bp)
    app.register_blueprint(pretrained_bp)
    app.register_blueprint(store_data_bp)
    return app

app = create_app()

if __name__ == "__main__":
    if app.debug:
        app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
