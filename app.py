import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from routes.rule_based import bp as paraphrase_bp

load_dotenv()
if(os.environ.get('ENVIRONMENT') == 'Local'):
    Flask.debug = True

def create_app():
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:8080', 'https://dylanhourigan.github.io'])

    # Register the blueprints
    app.register_blueprint(paraphrase_bp)

    return app

app = create_app()

if __name__ == "__main__":
    if app.debug:
        app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
