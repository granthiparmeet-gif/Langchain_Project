def peek (docs, n=1):
    for i, d in enumerate(docs[:n], 1):
        print(f"\n--- DOC {i} ---")
        print("CONTENT:", (d.page_content[:300] + "…") if len(d.page_content)>300 else d.page_content)
        print("META   :", d.metadata)