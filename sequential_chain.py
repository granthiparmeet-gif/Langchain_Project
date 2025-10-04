from langchain.chains import SequentialChain, LLMChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

# Chain 1: Generate company name
prompt1 = PromptTemplate(
    input_variables=["product"],
    template="Suggest a creative company name for {product}."
)
chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="company_name")

# Chain 2: Generate tagline
prompt2 = PromptTemplate(
    input_variables=["company_name"],
    template="Create a tagline for {company_name}."
)
chain2 = LLMChain(llm=llm, prompt=prompt2, output_key="tagline")

# SequentialChain with multiple inputs/outputs
overall_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["product"],
    output_variables=["company_name", "tagline"],
    verbose=True
)

result = overall_chain({"product": "eco-friendly water bottle"})
print(result)
