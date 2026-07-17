from flask import Flask
from flask_cors import CORS
from pathlib import Path

from api.routes import translation_bp
from config import Config


def create_app():
    BASE_DIR = Path(__file__).resolve().parent.parent

    app = Flask(
        __name__,
        template_folder=str(BASE_DIR / "templates"),
        static_folder=str(BASE_DIR / "static"),
        )

    CORS(app)

    app.config["UPLOAD_FOLDER"] = Config.UPLOAD_FOLDER

    app.register_blueprint(translation_bp)

    return app