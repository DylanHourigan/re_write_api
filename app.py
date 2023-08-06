from flask import Flask
from routes.rule_based import bp as paraphrase_bp

def create_app():
    app = Flask(__name__)

    # Register the blueprints
    app.register_blueprint(paraphrase_bp)

    return app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)