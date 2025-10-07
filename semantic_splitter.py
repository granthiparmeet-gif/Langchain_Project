# from langchain_experimental.text_splitter import SemanticChunker
# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv


# load_dotenv()

# text = """
# Galaxies form vast systems of stars, dust, and dark matter held together by gravity. 
# Our Milky Way is one of billions in the observable universe. 
# At the heart of many galaxies lie supermassive black holes that influence the formation and motion of stars. 
# Scientists continue to study dark energy, which drives the universe’s accelerated expansion.

# Artificial Intelligence, on the other hand, has transformed nearly every modern industry. 
# Large language models like GPT-4 and Claude are capable of writing, reasoning, and assisting in creative tasks. 
# AI is increasingly used in healthcare, education, and law — but also raises questions about bias, privacy, and alignment with human values. 
# Researchers are exploring multi-agent systems, retrieval-augmented generation, and autonomous workflows to make AI more interpretable and useful.

# Meanwhile, human health and medicine continue to evolve rapidly. 
# Genomic sequencing allows doctors to predict and prevent diseases at the DNA level. 
# Advancements in neuroscience are unlocking treatments for mental disorders like depression and anxiety. 
# However, ethical questions remain about genetic editing and access to healthcare in developing countries.

# History reminds us that technology revolutions always reshape society. 
# The Industrial Revolution gave rise to cities, railways, and mass production. 
# The Digital Revolution connected billions through the internet. 
# Now, the AI Revolution is set to redefine work, creativity, and communication on a global scale.

# In the world of technology infrastructure, quantum computing and renewable energy stand out as the next frontiers. 
# Quantum systems promise exponential computational power, while solar and fusion research aim to solve humanity’s energy crisis. 
# Together, these technologies may determine the sustainability of civilization itself.
# """


# embeddings = OpenAIEmbeddings()  # or any embedding model you have
# splitter = SemanticChunker(
#     embeddings=embeddings,
#     buffer_size=1,
#     breakpoint_threshold_type="percentile",
#     # you can also set min_chunk_size etc.
# )

# chunks = splitter.split_text(text)
# for c in chunks:
#     print("SEMANTIC CHUNK:", c)



from langchain_openai import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv

load_dotenv()


text = """
Galaxies form vast systems of stars, dust, and dark matter held together by gravity. 
Our Milky Way is one of billions in the observable universe. 
At the heart of many galaxies lie supermassive black holes that influence the formation and motion of stars. 
Scientists continue to study dark energy, which drives the universe’s accelerated expansion.

Artificial Intelligence, on the other hand, has transformed nearly every modern industry. 
Large language models like GPT-4 and Claude are capable of writing, reasoning, and assisting in creative tasks. 
AI is increasingly used in healthcare, education, and law — but also raises questions about bias, privacy, and alignment with human values. 
Researchers are exploring multi-agent systems, retrieval-augmented generation, and autonomous workflows to make AI more interpretable and useful.

Meanwhile, human health and medicine continue to evolve rapidly. 
Genomic sequencing allows doctors to predict and prevent diseases at the DNA level. 
Advancements in neuroscience are unlocking treatments for mental disorders like depression and anxiety. 
However, ethical questions remain about genetic editing and access to healthcare in developing countries.

History reminds us that technology revolutions always reshape society. 
The Industrial Revolution gave rise to cities, railways, and mass production. 
The Digital Revolution connected billions through the internet. 
Now, the AI Revolution is set to redefine work, creativity, and communication on a global scale.

In the world of technology infrastructure, quantum computing and renewable energy stand out as the next frontiers. 
Quantum systems promise exponential computational power, while solar and fusion research aim to solve humanity’s energy crisis. 
Together, these technologies may determine the sustainability of civilization itself.
"""


splitter = SemanticChunker(
    OpenAIEmbeddings()
)

chunks = splitter.split_text(text)

for i,c in enumerate(chunks,1):
    print("SEMANTIC CHUNK:", c)