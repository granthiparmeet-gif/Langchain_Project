from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_template("Write a joke on {topic}")

chain = prompt | llm | StrOutputParser()

print(chain.invoke({"topic":"cat"}))
