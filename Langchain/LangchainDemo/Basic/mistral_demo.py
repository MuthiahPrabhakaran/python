from langchain_ollama import ChatOllama

llm = ChatOllama(model="mistral")
question = input("Enter the question\n")
response = llm.invoke(question)
print(response.content)