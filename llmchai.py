from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

prompt = PromptTemplate.from_template("Whats the Capital of {country}")

chain = LLMChain(
    llm=llm,
    prompt=prompt
)

print(chain.run(country="India"))