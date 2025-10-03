from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage("You are a expert socail media manager"),
    HumanMessage("Give a short tip to create engaging post on Instagram")
]

llm = ChatOpenAI()

result= llm.invoke(messages)

print(result.content)