from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import AIMessage

load_dotenv()

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("placeholder", "{history}"),
        ("human", "{question}")
    ]
)

chain = prompt | llm

store = {}

def chat_history(session_id :str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory ()
    history = store[session_id]

    if len(history.messages) > 6:
        old_chat = "\n".join(m.content for m in history.messages[:-4])
        summary = llm.invoke(f"Summarize this in 1-2 lines {old_chat}").content

        history.messages = [AIMessage(content={summary})] + history.messages[-4:]

    return history

chain_with_summary = RunnableWithMessageHistory(
    chain,
    chat_history,
    input_messages_key="question",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "user_123"}}

print(chain_with_summary.invoke({"question":"I love playing football."}, config=config).content)
print(chain_with_summary.invoke({"question": "Also, I enjoy hiking on weekends."}, config=config).content)
print(chain_with_summary.invoke({"question": "Can you summarize what I told you?"}, config=config).content)

