from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st

prompt = PromptTemplate(
    input_variables=["company", "position", "strengths", "weaknesses"],
    template="""You are a career coach. Provide tailored interview tips for the
    position of {position} at {company}.
    Highlight your strengths in {strengths} and prepare for questions
    about your weaknesses such as {weaknesses}.
    """
)

llm = ChatOllama(model="mistral")

st.title("Interview Tips Generator")

company = st.text_input("Company Name")
position = st.text_input("Position Title")
strength = st.text_area("Enter your Strengths", height=100)
weakness = st.text_area("Enter your Weaknesses", height=100)

if company and position and strength and weakness:
    response = llm.invoke(prompt.format(company=company, position=position, strengths=strength, weaknesses=weakness))
    st.write(response)
