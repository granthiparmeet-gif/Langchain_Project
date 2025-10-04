from langchain.chains import SimpleSequentialChain, LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")


prompt1 = PromptTemplate(
    template="Write a short poem on {topic}",
    input_variables=["topic"]
)
chain1 = LLMChain(llm=llm, prompt=prompt1)


prompt2 = PromptTemplate(
    template="Summarize this poem in one line: {poem}",
    input_variables=["poem"]
)
chain2 = LLMChain(llm=llm, prompt=prompt2)


overall = SimpleSequentialChain(chains=[chain1, chain2], verbose=True)

print(overall.run("the moon"))
