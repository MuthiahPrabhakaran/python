from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st


llm = ChatOllama(model="mistral")
prompt_template = PromptTemplate(
    input_variables = ["country", "no_of_paras", "language"],
    template = """You are an expert in traditional cuisines.
    You provide information about a specific dish from a specific country.
    Avoid giving information about fictional places. If the country is fictional
    or non-existent answer: I don't know. Don't give any more details. I want a simple I don't know as an answer.
    Answer the question: What is the traditional cuisine of {country}?
    Answer in {no_of_paras} short paras in {language}
    """
)

st.title("Cuisine Info")
country = st.text_input("Enter the country:")
no_of_paras = st.number_input("Enter the number of paras that you want to see in the result:",
                              min_value = 1, max_value = 5)
language = st.text_input("Enter the language that you want to see the result:")

if country:
    response = llm.invoke(prompt_template.format(country=country, no_of_paras=no_of_paras,
                                                 language=language))
    st.write(response)