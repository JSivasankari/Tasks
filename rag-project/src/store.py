import chromadb

def get_collection(reset=False):
    client = chromadb.PersistentClient(path="chroma_db")
    if reset:
        try:
            client.delete_collection("docs")
        except Exception:
            pass
    # Chroma's default embedder: all-MiniLM-L6-v2 (local, free, no API key)
    return client.get_or_create_collection("docs", metadata={"hnsw:space": "cosine"})
