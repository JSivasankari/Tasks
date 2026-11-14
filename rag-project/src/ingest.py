import glob, os
from chunker import chunk_text
from store import get_collection

col = get_collection(reset=True)
total = 0
for path in sorted(glob.glob("data/*.md")):
    name = os.path.basename(path)
    chunks = chunk_text(open(path, encoding="utf-8").read())
    col.add(
        ids=[f"{name}-{i}" for i in range(len(chunks))],
        documents=chunks,
        metadatas=[{"source": name, "chunk": i} for i in range(len(chunks))],
    )
    total += len(chunks)
    print(f"{name}: {len(chunks)} chunks")
print(f"Stored {total} chunks in Chroma.")
