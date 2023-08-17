import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from routes.models.rule_based import bp as rule_based_bp
from routes.models.pre_trained import bp as pretrained_bp
from routes.auth.login import bp as login_bp

load_dotenv()
if(os.environ.get('ENVIRONMENT') == 'Local'):
    Flask.debug = True

def create_app():
    applicationlication = Flask(__name__)
    CORS(application, origins=['http://localhost:8080', 'https://dylanhourigan.github.io'])

    applicationlication.register_blueprint(rule_based_bp)
    application.register_blueprint(pretrained_bp)
    application.register_blueprint(login_bp)

    return application

application = create_app()

if __name__ == "__main__":
    if application.debug:
        application.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
