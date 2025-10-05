from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template("Give me a Json with 'country' and 'capital' for {continent}")

llm = ChatOpenAI()

chain = prompt | llm | JsonOutputParser()

result = chain.invoke({"continent": "Africa"})
print(result)