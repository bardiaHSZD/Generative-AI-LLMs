from src.langgraphagenticai.state.state import State
from langchain_core.messages import HumanMessage, ToolMessage

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    """
    def __init__(self,model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a response with tool integration.
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        # Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}
    

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        def chatbot_node(state: State):
            """
            Chatbot logic for processing input state with web tool results.
            """
            user_input = state["messages"][-1] if state["messages"] else ""
            query = user_input.content if hasattr(user_input, "content") else str(user_input)

            search_tool = tools[0] if tools else None
            tool_output = search_tool.invoke({"query": query}) if search_tool else ""

            ai_response = self.llm.invoke(
                [
                    HumanMessage(
                        content=(
                            f"User question: {query}\n\n"
                            f"Web search results: {tool_output}\n\n"
                            "Provide a concise and accurate answer based on these results."
                        )
                    )
                ]
            )

            return {
                "messages": [
                    HumanMessage(content=query),
                    ToolMessage(content=str(tool_output), tool_call_id="tavily_search"),
                    ai_response,
                ]
            }

        return chatbot_node


