import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Missing OPENAI_API_KEY in .env")
    sys.exit(1)


llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=api_key
)


memory = ConversationBufferMemory()


prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""You are a helpful chatbot.
Remember conversation history and reply clearly.

Conversation so far:
{history}

User: {input}
Bot:"""
)


conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt
)

print("🤖 Chatbot with memory (type 'exit' to quit)")

try:
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = conversation.run(user_input)
        print("Bot:", response)

except KeyboardInterrupt:
    print("\nChat ended by user.")