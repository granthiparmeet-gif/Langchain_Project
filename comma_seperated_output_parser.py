from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template("Give me a list of {question}")

llm = ChatOpenAI()

chain = prompt | llm | CommaSeparatedListOutputParser()

result = chain.invoke({"question": "countries in Asia"})
print(result)