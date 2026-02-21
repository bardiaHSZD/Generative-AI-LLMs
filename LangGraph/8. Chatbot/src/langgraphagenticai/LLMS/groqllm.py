from langchain_community.chat_models import ChatOllama


class OllamaLLM:
    def __init__(self, user_contols_input):
        self.user_controls_input = user_contols_input

    def get_llm_model(self):
        try:
            selected_ollama_model = self.user_controls_input.get("selected_ollama_model", "qwen2.5:7b")
            llm = ChatOllama(model=selected_ollama_model)
        except Exception as e:
            raise ValueError(f"Error Ocuured With Exception : {e}")
        return llm


# Backward-compatible alias for older imports
GroqLLM = OllamaLLM