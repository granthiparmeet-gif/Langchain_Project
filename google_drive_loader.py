from langchain_community.document_loaders import GoogleDriveLoader


loader = GoogleDriveLoader(
    file_ids=["1dQD_WZ0kEU7bJ7k_gK9IdleaB__kBz9L0PtCtdA17fg"],
    credentials_path="/Users/parmeetsingh/Desktop/Langchain- Projects/client_secret_975786706033-g77ho1uk42qooo4i3der904lffivdqn5.apps.googleusercontent.com.json",  # Path to your credentials file
)

docs = loader.load()

for i, d in enumerate(docs, 1):
    print(f"--- DOCUMENT {i} ---")
    print(d.page_content[:500])  # Show preview
    print("Metadata:", d.metadata)
    print()



