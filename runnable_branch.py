from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch

load_dotenv()

llm = ChatOpenAI()

joke_prompt = ChatPromptTemplate.from_template("Write a joke on {topic}")
joke_chain = joke_prompt | llm

fact_prompt = ChatPromptTemplate.from_template("Write a fact on {topic}")
fact_chain = fact_prompt | llm

default_prompt = ChatPromptTemplate.from_template("I can only tell you joke or fact")
default_chain = default_prompt | llm

chain = RunnableBranch(
  (lambda x:"joke" in x["mode"], joke_chain),
  (lambda x:"fact" in x["fact"], fact_chain),
  default_chain
)

result = chain.invoke({
    "mode":"joke",
    "topic":"cat"
})

print(result.content)