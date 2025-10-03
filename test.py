from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o-mini"
)
#Using Invoke
print(llm.invoke("Give me Information on India?").content)


#Using Stream
result = llm.stream("Give me Information on India")

for parts in result:
    print(parts.content, end="", flush=True)


#Using Batch
result = llm.batch(["Give me Information on India", "Give me information on France"])

for parts in result:
    print(parts.content)