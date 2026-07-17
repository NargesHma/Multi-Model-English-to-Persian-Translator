import requests
from requests.exceptions import HTTPError, Timeout, RequestException
from utils.logger import logger

from config import Config



class MetisTranslator:
    """
    Translator service for Metis AI API
    Responsible only for communicating with metis
    """

    BASE_URL = "https://api.metisai.ir/api/v1/chat/{provider}/completions"

    def __init__(self):
        self.api_key = Config.METIS_API_KEY
        self.provider = Config.MODEL_PROVIDER
        self.model_name = Config.MODEL_NAME

    def translate(self, text: str) -> str:
        """
        Translate English text to Persian
        """

        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a professional English to Persian translator. Translate naturally using informal Persian"
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        }

        url = self.BASE_URL.format(provider=self.provider)
        try:
            response = requests.post(
                url=url,
                headers=headers,
                json=payload,
                timeout=60
            )

            response.raise_for_status()

            translated_text = response.json()["choices"][0]["message"]["content"]

            logger.info("Translation completed successfully.")

            return translated_text
        
        except Timeout:
            logger.error("Metis API timeout.")
            raise Exception("Translation service timed out.")
        
        except HTTPError as e:
            logger.error(f"HTTP Error: {e}")
            raise Exception("Translation service returned an HTTP error.")
        
        except RequestException as e:
            logger.error(f"Request Error: {e}")
            raise Exception("Unable to connect to Metis API.")
        
        except Exception as e:
            logger.exception(e)
            raise