import requests
import streamlit as st


def get_ollama_response(input_text):
    json_body={
  "input": {
    "language": "French",
    "text": input_text
  },
  "config": {},
  "kwargs": {}
}
    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body, timeout=60)
    response.raise_for_status()
    data = response.json()
    return data.get("output", "")

## Streamlit app
st.title("LLM Application Using LCEL")
input_text=st.text_input("Enter the text you want to convert to french")

if input_text:
    st.write(get_ollama_response(input_text))