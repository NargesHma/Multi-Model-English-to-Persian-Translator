from services.bart_service import MBartTranslator
from services.llm_service import MetisTranslator


class TranslationService:

    def __init__(self):
        
        self.translators = {
            "llm": MetisTranslator(),
            "bart": MBartTranslator(),
        }

    def translate(self, model: str, text: str) -> str:

        translator = self.translators.get(model)

        if translator is None:
            raise ValueError(f"Unsupported model: {model}")
        
        return translator.translate(text)