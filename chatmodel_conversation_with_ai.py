from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

chat_history=[]

chat_history.append(SystemMessage(content="You are a helpful assistant"))

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    chat_history.append(HumanMessage(content=user_input))
    result = llm.invoke(chat_history)
    print("AI: ", result.content)

    chat_history.append(result)