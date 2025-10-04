from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

example = [
    {"country":"India", 
     "capital":"New Delhi"},
    {"country":"Pakistan", 
     "capital":"Islamabad"}
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("user", "What is the Capital of {country}"),
        ("assistant", "The capital of {country} is {capital}.")
    ]
)

few_shot = FewShotChatMessagePromptTemplate(
    examples=example,
    example_prompt = example_prompt
)

final_prompt = ChatPromptTemplate.from_messages(
    [("system","You are a helpful assistant"),
     few_shot,
     ("user", "What is the Capital of {country}")
])

prompt= final_prompt.format_messages(country = "Japan")
result = llm.invoke(prompt)

print(result.content)