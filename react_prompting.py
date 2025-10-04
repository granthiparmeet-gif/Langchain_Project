from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

react_prompt = """
You are a smart assistant that uses React Pattern.

use the following format:

Question: The input that you must answer
Thought: Reasoning what to do
Action: The action to take if needed
Observation:  the result of the action

You can reapeat (Thought/Action/Observation)

Final Answer: The final answer to the question

Here is an example:

Question: What is 5 + 3?
Thought: I should add the two numbers.
Action: calculate 5+3
Observation: 8
Thought: Now I know the answer.
Final Answer: 8

Now, follow the same format.

Question: Who is the CEO of OpenAI?

"""

response = llm.invoke(react_prompt)
print(response.content)