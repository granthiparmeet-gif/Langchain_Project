from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory


load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant.Always remember what the user said earlier and use that memory to answer follow-up questions."),
    ("placeholder", "{history}"),
    ("human", "{input}")
]
)


chain = prompt | llm

store = {}

def chat_history(session_id : str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    history = store[session_id]

    if len(history.messages)>2:
        history.messages = history.messages[-2:]
    return history

chat_with_history = RunnableWithMessageHistory(
    chain,
    chat_history,
    input_messages_key="input",
    history_messages_key="history"
)

config  = {"configurable":{"session_id":"user_123"}}

print(chat_with_history.invoke({"input": "My name is Parmeet."}, config=config).content)
print(chat_with_history.invoke({"input": "I live in India."}, config=config).content)
print(chat_with_history.invoke({"input": "I love cricket."}, config=config).content)
print(chat_with_history.invoke({"input": "What did I tell you so far?"}, config=config).content)
