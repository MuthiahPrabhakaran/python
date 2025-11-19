from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st


llm = ChatOllama(model="mistral:latest")
prompt_template = PromptTemplate(
    input_variables = ["city", "month", "language" , "budget"],
    template = """Welcome to the {city} travel guide!
            If you're visiting in {month}, here's what you can do:
            1. Must-visit attractions.
            2. Local cuisine you must try.
            3. Useful phrases in {language}.
            4. Tips for traveling on a {budget} budget.
            Enjoy your trip!
    """
)

st.title("Travel Guide")
city = st.text_input("Enter the city:")
month = st.text_input("Enter the month of travel:")
language = st.text_input("Enter the language that you want to see the result:")
budget = st.selectbox("Travel Budget", ["Low", "Medium", "High"])

chain = prompt_template | llm

if city and month and language and budget:
    response = chain.invoke({"city":city, "month":month,
                                                 "language":language, "budget":budget})
    st.write(response)