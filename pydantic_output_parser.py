from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

class Person(BaseModel):
    name : str = Field(... , description="The persons full age")
    age : int = Field(23, description="His age")
    hobby: str = Field(description="One hobby they enjoy")

parser = PydanticOutputParser(pydantic_object=Person)

prompt = ChatPromptTemplate.from_template("Get deatils of a fictional person in JSON\n.{format}")

chain = prompt | llm | parser

response = chain.invoke({"format":parser.get_format_instructions()})

print(response)

