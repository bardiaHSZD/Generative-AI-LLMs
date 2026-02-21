import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from langchain_community.chat_models import ChatOllama
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.

    """

    ##Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            ## Configure The LLM's
            selected_ollama_model = user_input.get("selected_ollama_model", "qwen2.5:7b")
            model=ChatOllama(model=selected_ollama_model)

            if not model:
                st.error("Error: LLM model could not be initialized")
                return
            
            # Initialize and set up the graph based on use case
            usecase=user_input.get("selected_usecase")

            if not usecase:
                    st.error("Error: No use case selected.")
                    return
            
            ## Graph Builder

            graph_builder=GraphBuilder(model)
            try:
                 normalized_usecase = (usecase or "").strip().lower().replace("-", " ").replace("_", " ")
                 if normalized_usecase == "chatbot with web":
                     tavily_key = user_input.get("TAVILY_API_KEY", "")
                     if not tavily_key:
                         st.error("Error: TAVILY_API_KEY is required for 'Chatbot With Web'.")
                         return

                 graph=graph_builder.setup_graph(usecase)
                 print(user_message)
                 DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                 error_msg = str(e).strip() or repr(e)
                 st.error(f"Error: Graph execution failed - {error_msg}")
                 return

        except Exception as e:
             st.error(f"Error: Graph set up failed- {e}")
             return   
