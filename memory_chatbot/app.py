from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

print("🤖 Chatbot with memory (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = conversation.run(user_input)
    print("Bot:", response)
