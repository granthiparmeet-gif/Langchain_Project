from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory


load_dotenv()

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant"),
    ("placeholder", "{history}"),
    ("human", "{input}")
]
)

chain = prompt| llm

store = {}

def get_history(session_id : str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chat_with_history = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key="input",
    history_messages_key="history"
)

config = {"configurable":{"session_id": "user_123"}}

result1 = (chat_with_history.invoke({"input":"Hi My name is Parmeet"}, config=config))
print(result1.content)

result2 = (chat_with_history.invoke({"input":"Whats my name"}, config=config))
print(result2.content)