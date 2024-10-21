import openai
from models.model_interface import ModelInterface


class GPT(ModelInterface):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo") -> None:
        self.openai = openai
        self.openai.api_key = api_key
        self.model = model

    def get_completion(self, prompt: str, temperature: int = 0):
        messages = [{"role": "user", "content": prompt}]
        response = self.openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message["content"]
