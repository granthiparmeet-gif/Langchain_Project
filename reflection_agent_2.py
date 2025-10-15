from typing import List, Sequence
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from reflection_agent import generation_chain, reflection_chain

load_dotenv()
graph = MessageGraph()