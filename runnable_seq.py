from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = ChatOpenAI()
prompt1 = ChatPromptTemplate.from_template("Write a short poem about {topic}")
poem_chain = prompt1 | llm

prompt2 = ChatPromptTemplate.from_template("Write a summary on {poem}")
summary_chain = prompt2 | llm


chain = RunnableSequence(first=poem_chain, last=summary_chain)

result = chain.invoke({"topic":"moon"})
print(result.content)
