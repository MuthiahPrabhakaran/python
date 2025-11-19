from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.globals import set_debug

set_debug(True)

llm = ChatOllama(model="mistral")

st.title("Ask Anything")
question = st.text_input("What is your question?")

if question:
    response = llm.invoke(question)
    st.write(response)