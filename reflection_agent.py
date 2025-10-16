from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

generate_prompt= ChatPromptTemplate.from_messages([
    ("system", "You are a twitter techie influence assistant tasked with writting excellent twitter post."
     "Generate the best twitter possible for the user requests."
     "If a user provides with a critique, respond witha revised version of your previous attempts"
     ),
     MessagesPlaceholder(variable_name="messages"),
])

reflection_prompt = ChatPromptTemplate.from_messages([
    ("system","You are a viral twitter inflencer who is grading tweets."
    "Generate critique and recommendations based for the users tweet."
    "Always provide detailed recommendations, length, virality etc"),
    MessagesPlaceholder(variable_name="messages")
])

generation_chain = generate_prompt | llm
reflection_chain = reflection_prompt | llm