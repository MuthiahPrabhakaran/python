from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma2:2b")

question = input("Enter the question")
response = llm.invoke(question)
print(response)
print(response.content)