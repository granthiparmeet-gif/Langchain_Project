from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, tool
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults
import datetime

load_dotenv()

llm = ChatOpenAI()
tavily_tool = TavilySearchResults(search_depth="basic")

@tool
def time_now(format : str = "%Y-%M-%D %H:%M:%S"):
    "Returns the current date and time in the specified format"
    current_time = datetime.datetime.now()
    format_time = current_time.strftime(format)
    return format_time

agent = initialize_agent(tools=[tavily_tool, time_now], llm=llm, agent="zero-shot-react-description", verbose = True)



agent.invoke("When was spaceX last launch , nad how many exact hors ago it was?")

