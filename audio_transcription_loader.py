from dotenv import load_dotenv
from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers.audio import OpenAIWhisperParser

# Load environment variables
load_dotenv()

# Path to your MP3 file
audio_path = "/Users/parmeetsingh/Desktop/Langchain- Projects/sample.mp3"

# Create blob loader
blob_loader = FileSystemBlobLoader(audio_path)

# Create Whisper parser (uses OpenAI Whisper API — requires OPENAI_API_KEY)
parser = OpenAIWhisperParser()

# Combine both
loader = GenericLoader(blob_loader, parser)

# Load and transcribe
docs = loader.load()

# Print transcribed text
for d in docs:
    print("TRANSCRIPT:\n", d.page_content[:300])
    print("METADATA:\n", d.metadata)
