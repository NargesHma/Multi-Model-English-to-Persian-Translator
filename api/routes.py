import json
import os
import pysrt
from flask import (Blueprint, Response, current_app, jsonify, render_template, request, stream_with_context)
from werkzeug.utils import secure_filename
from services.translation_service import TranslationService


translation_bp = Blueprint("translation", __name__)
translation_service = TranslationService()


@translation_bp.route("/")
def home():
    return render_template("index.html")


@translation_bp.route("/upload_file", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return jsonify({"error": "No File"}), 400
    
    file = request.files["file"]

    filename = secure_filename(file.filename)

    path = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        filename,
    )

    file.save(path)

    return jsonify({"message": "Uploaded"})


@translation_bp.route("/translate_text/<model>", methods=["POST"])
def translate_text(model):

    body = request.get_json()

    translated = translation_service.translate(
        model=model,
        text=body["text"]
    )

    return jsonify(
        {
            "translated_text": translated
        }
    )


@translation_bp.route("/translate_line/<model>")
def translate_line(model):

    uploaded = os.listdir(
        current_app.config["UPLOAD_FOLDER"]
    )

    latest = max(
        [
            os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                f,
            )
            for f in uploaded
        ],
        key=os.path.getctime,
    )

    subtitles = pysrt.open(latest)

    @stream_with_context
    def generate():

        for subtitle in subtitles:

            translated = translation_service.translate(
                model=model,
                text=subtitle.text,
            )

            yield (
                "data:"
                +json.dumps(
                    {
                        "index": subtitle.index,
                        "original_text": subtitle.text,
                        "translated_text": translated,
                    }
                )
                + "\n\n"
            )
        
    return Response(
        generate(),
        content_type="text/event-stream",
    )