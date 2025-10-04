# from langchain.prompts import PromptTemplate

# template = "Tell me a joke about {Topic}"
# prompt = PromptTemplate.from_template(template)

# final_prompt = prompt.format(Topic = "India")

# print(final_prompt)

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatOpenAI()

# a = ChatPromptTemplate.from_messages([
#     ("system","You are a {role}"),
#     ("human", "Tell me {adj} on {topic}")
# ])

# messages = a.format_messages(role = "comedian", adj = "joke", topic = "India")

# result = llm.invoke(messages)
# print(result.content)

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

sys_message = SystemMessagePromptTemplate.from_template("You are a {role}")
user_message = HumanMessagePromptTemplate.from_template("Tell me {adj} on {topic}")

chat_prompt = ChatPromptTemplate.from_messages([sys_message, user_message])

messages = chat_prompt.format_messages(role = "Helpful assistant", adj= "fun fact", topic= "India")

result = llm.invoke(messages)
print(result.content)