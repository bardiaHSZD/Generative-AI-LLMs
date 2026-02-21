import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())


        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Ollama':
                # Model selection
                self.user_controls["selected_ollama_model"] = "qwen2.5:7b"
                st.caption("Using Ollama model: qwen2.5:7b")
            
            ## USecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases",usecase_options)

        return self.user_controls