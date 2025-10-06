from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

load_dotenv()
llm = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("Summarize this text in one line {text}")

def word_count(message):
    text = message.content if hasattr(message, "content") else str(message)
    return f" The summary has {len(text.split())} words "


word_counter =RunnableLambda(word_count)

chain = prompt | llm | word_counter

print(chain.invoke({"text": "LangChain helps developers build powerful LLM-based apps easily."}))