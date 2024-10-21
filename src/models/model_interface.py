class ModelInterface:
    def get_completion(self, prompt: str, temperature: int = 0):
        raise NotImplementedError("This method should be overridden by subclasses")
