from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

# Define message templates
sys_message = ChatMessagePromptTemplate.from_template(
    template="You are a {role}.",
    role="system"
)

human_message = ChatMessagePromptTemplate.from_template(
    template="Tell me a {adj} on {topic}.",
    role="user"
)

# Build the full prompt template
prompt = ChatPromptTemplate.from_messages([sys_message, human_message])

# Fill placeholders and get messages
messages = prompt.format_messages(role="helpful assistant", adj="fun fact", topic="India")

# Call the model
result = llm.invoke(messages)
print(result.content)
