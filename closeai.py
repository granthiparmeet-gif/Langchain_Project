from langchain_openai import OpenAIAudioTranscriptionLoader


loader = OpenAIAudioTranscriptionLoader(
    file_path="/Users/parmeetsingh/Desktop/Langchain- Projects/sample.mp3",
    model="gpt-4o-mini-transcribe" 
)

# Transcribe
docs = loader.load()

# Show transcription
for i, d in enumerate(docs, 1):
    print(f"--- TRANSCRIPT {i} ---")
    print(d.page_content[:300])
    print("Metadata:", d.metadata)
