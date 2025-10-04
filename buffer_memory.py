from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

llm = ChatOpenAI()

memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(
    llm= llm,
    memory = memory,
    verbose = True
)

print(conversation.run("Hello, I am Parmeet Singh"))
print(conversation.run("Where I am from?"))
print(conversation.run("What did I tell you earlier?"))