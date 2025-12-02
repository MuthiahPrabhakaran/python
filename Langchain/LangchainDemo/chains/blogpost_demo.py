from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

llm = ChatOllama(model="llama3.1:8b")

outline_prompt = PromptTemplate(input_variables=["topic"],
                                template="""
                                You are a professional blogger.
                                Create an outline for a blog post on the following topic: {topic}
                                The outline should include:
                                - Introduction
                                - 3 main points with subpoints
                                - Conclusion
                                """)

introduction_prompt = PromptTemplate(input_variables=["outline"],
                                     template="""
                                     You are a professional blogger.
                                     Write an engaging introduction paragraph based on the following
                                     outline:{outline}
                                     The introduction should hook the reader and provide a brief
                                     overview of the topic.
                                     """)

first_chain = outline_prompt | llm | StrOutputParser() | (lambda topic:(st.write(topic), topic)[1])
second_chain = introduction_prompt | llm
overall_chain = first_chain | second_chain

st.title("Blogpost Generator")
topic = st.text_input("Enter the input topic")

if topic:
    response = overall_chain.invoke({"topic":topic})
    st.write(response)