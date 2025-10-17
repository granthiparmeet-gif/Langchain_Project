from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI()


summar_prompt = ChatPromptTemplate.from_template("Write the summary about given {text}")
summar_chain = summar_prompt | llm

senti_prompt = ChatPromptTemplate.from_template("Write the sentiment about  {text}")
senti_chain = senti_prompt | llm

chain = RunnableParallel(
    summary = summar_chain,
    sentiment = senti_chain
)

text = "The new city park is a fantastic addition to our community! The playgrounds are vibrant and safe, the walking paths are well-maintained, and there's a beautiful pond for relaxing. My only complaint is that the new cafe is a bit overpriced, but overall, it's a wonderful place to spend an afternoon"
result = chain.invoke(text)

print("Summary:" , result["summary"].content)
print("Sentiment:" , result["sentiment"].content)