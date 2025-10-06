from langchain_community.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=jGwO_UgTS7I",  
    add_video_info=False
)

docs = loader.load()

print("Transcript Preview:\n", docs[0].page_content[:400])
