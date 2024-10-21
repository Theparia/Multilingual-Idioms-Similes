import google.generativeai as genai
from models.model_interface import ModelInterface
from google.generativeai.types import HarmCategory, HarmBlockThreshold


class Gemini(ModelInterface):
    def __init__(self, api_key: str, model: str = "gemini-1.5-flash") -> None:
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    def get_completion(self, prompt: str) -> str:
        response = self.model.generate_content(
            prompt,
            safety_settings=[
                {
                    "category": HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                    "threshold": HarmBlockThreshold.BLOCK_NONE,
                },
                {
                    "category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                    "threshold": HarmBlockThreshold.BLOCK_NONE,
                },
                {
                    "category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                    "threshold": HarmBlockThreshold.BLOCK_NONE,
                },
                {
                    "category": HarmCategory.HARM_CATEGORY_HARASSMENT,
                    "threshold": HarmBlockThreshold.BLOCK_NONE,
                },
            ],
        )
        return response.text
