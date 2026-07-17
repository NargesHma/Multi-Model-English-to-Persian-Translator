from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from config import Config

class MBartTranslator:

    def __init__(self):
        
        self.tokenizer = MBart50TokenizerFast.from_pretrained(
            Config.BART_MODEL_NAME
        )

        self.model = MBartForConditionalGeneration.from_pretrained(
            Config.BART_MODEL_NAME
        )

        self.tokenizer.src_lang = "en_XX"

        self.tokenizer.tgt_lang = "fa-IR"
    
    def translate(self, text: str) -> str:

        encoded = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=128
        )

        generated = self.model.generate(
            **encoded,
            max_length=128,
            num_beams=4,
            early_stopping=True,
            forced_bos_token_id=self.tokenizer.lang_code_to_id["fa_IR"]
        )

        return self.tokenizer.decode(
            generated[0],
            skip_special_tokens=True
        )