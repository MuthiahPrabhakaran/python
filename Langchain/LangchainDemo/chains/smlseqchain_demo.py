from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3.1:8b")

title_prompt = PromptTemplate(input_variables=["topic"],
                              template="""You are an experienced speech writer.
                              You need to craft an impactful title for a speech
                              on the following topic: {topic}
                              Answer exactly with one title.
                              """)

speech_prompt = PromptTemplate(input_variables=["title"],
                              template= """You need to write a powerful speech of 350 words
                                           for the following title: {title}
                              """)

# StrOutputParser will filter the content part alone from the response
first_chain = title_prompt | llm | StrOutputParser() | (lambda title:(st.write(title), title)[1])
second_chain = speech_prompt | llm
# output of first chain will be passed to the second chain
final_chain = first_chain | second_chain

st.title("Speech Generator")

topic = st.text_input("Enter the topic for the speech generator")

if topic:
    response = final_chain.invoke({"topic":topic})
    st.write(response)