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

# Optional: custom prompt template
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

print("🤖 Chatbot with memory (type 'exit' or Ctrl+C to quit)")
try:
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        try:
            response = conversation.run(user_input)
            print(f"Bot ({datetime.now().strftime('%H:%M:%S')}): {response}")
        except Exception as e:
            print(f" Error: {e}")

except KeyboardInterrupt:
    print("\n Chat ended by user.")