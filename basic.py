from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("Write a short poem about {topic}")

chain = prompt | llm
response = chain.invoke({"topic": "sunsets"})

print(response.content)
