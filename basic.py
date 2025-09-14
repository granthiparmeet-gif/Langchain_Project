from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("Write a short poem about {topic}.")
formatted_prompt = prompt.format_messages(topic="sunsets")
response = llm(formatted_prompt)
print(response.content)