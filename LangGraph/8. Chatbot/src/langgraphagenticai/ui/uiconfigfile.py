from configparser import ConfigParser


class Config:
    def __init__(self,config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_ollama_model_options(self):
        models = self.config["DEFAULT"].get("OLLAMA_MODEL_OPTIONS")
        if not models:
            models = self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS", "qwen2.5:7b")
        return models.split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
