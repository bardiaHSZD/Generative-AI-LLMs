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
        if "timeframe" not in st.session_state:
            st.session_state.timeframe = ""
        if "IsFetchButtonClicked" not in st.session_state:
            st.session_state.IsFetchButtonClicked = False


        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Ollama':
                # Model selection
                model_options = self.config.get_ollama_model_options()
                self.user_controls["selected_ollama_model"] = st.selectbox("Select Model", model_options)
            
            ## USecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases",usecase_options)
            normalized_usecase = (self.user_controls["selected_usecase"] or "").strip().lower().replace("-", " ").replace("_", " ")

            if normalized_usecase in ["chatbot with web", "ai news"]:
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]=st.text_input("TAVILY API KEY",type="password")

                # Validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")

            if normalized_usecase == "ai news":
                st.subheader("📰 AI News Explorer ")
                
                with st.sidebar:
                    time_frame = st.selectbox(
                        "📅 Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0
                    )
                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame


        return self.user_controls