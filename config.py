import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    METIS_API_KEY = os.getenv("METIS_API_KEY")
    MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "open_ai_chat_completion")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o")

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER","uploads")

    BART_MODEL_NAME = os.getenv("BART_MODEL_NAME", "facebook/mbart-large-50-many-to-many-mmt")
