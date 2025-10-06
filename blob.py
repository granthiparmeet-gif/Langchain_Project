# pip install langchain langchain-community openai python-dotenv

from dotenv import load_dotenv
from langchain_core.document_loaders.blob_loaders import Blob
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.blob_loaders.file_system import FileSystemBlobLoader
from langchain_community.document_loaders.parsers.audio import OpenAIWhisperParser

# Load environment variables (make sure OPENAI_API_KEY is in your .env file)
load_dotenv()

# Path to your audio file
audio_path = "/Users/parmeetsingh/Desktop/Langchain- Projects/sample.mp3"

# Initialize blob loader and parser
blob_loader = FileSystemBlobLoader(path=audio_path)
parser = OpenAIWhisperParser()

# Combine into a generic loader
loader = GenericLoader(blob_loader, parser)

# Load and parse the audio file into text documents
docs = loader.load()

# Print partial content and metadata
for d in docs:
    print(d.page_content[:300])
    print(d.metadata)
