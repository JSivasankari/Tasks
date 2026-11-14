import sys
from store import get_collection

def retrieve(question, k=4):
    r = get_collection().query(query_texts=[question], n_results=k)
    return [
        {"source": m["source"], "text": d, "distance": dist}
        for d, m, dist in zip(r["documents"][0], r["metadatas"][0], r["distances"][0])
    ]

if __name__ == "__main__":  # sanity-check retrieval before wiring up the LLM
    q = " ".join(sys.argv[1:]) or "How long is the war room bridge named?"
    for h in retrieve(q):
        print(f"[{h['source']}] dist={h['distance']:.3f}\n{h['text'][:300]}...\n")
