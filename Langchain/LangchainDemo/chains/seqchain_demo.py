from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

llm = ChatOllama(model="llama3.1:8b")

title_prompt = PromptTemplate(input_variables=["topic"],
                              template="""You are an experienced speech writer.
                              You need to craft an impactful title for a speech
                              on the following topic: {topic}
                              Answer exactly with one title.
                              """)

speech_prompt = PromptTemplate(input_variables=["title", "emotion"],
                              template= """You need to write a powerful {emotion} speech of 350 words
                                           for the following title: {title}
                                           Format the output with 2 keys: 'title', 'speech' and fill them
                                           with the respective values
                              """)

# StrOutputParser will filter the content part alone from the response
first_chain = title_prompt | llm | StrOutputParser() | (lambda title:(st.write(title), title)[1])
second_chain = speech_prompt | llm | JsonOutputParser()
# output of first chain will be passed to the second chain
final_chain = first_chain | (lambda title: {"title": title, "emotion": emotion}) | second_chain

st.title("Speech Generator")

topic = st.text_input("Enter the topic for the speech generator")
emotion = st.text_input("Enter the emotion for the speech generator")

if topic and emotion:
    response = final_chain.invoke({"topic":topic})
    st.write(response)
    st.write(response['title'])