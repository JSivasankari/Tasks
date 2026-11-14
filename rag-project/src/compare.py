from rag import plain, rag

QUESTIONS = [
    "What is the name of the voice bridge opened for a SEV-1 incident at Nimbus Labs?",
    "How long does a KeyKeeper privileged access grant last at most at Nimbus Labs?",
    "What is the maximum bug bounty reward at Nimbus Labs?",
    "How many days must a critical-risk finding be fixed in at Nimbus Labs, and what tool scans weekly?",
]

out = ["# With RAG vs. without RAG\n"]
for q in QUESTIONS:
    answer, hits = rag(q)
    out += [f"## Q: {q}\n", f"**Without RAG:** {plain(q)}\n",
            f"**With RAG:** {answer}\n",
            f"_Top chunk: {hits[0]['source']} (distance {hits[0]['distance']:.3f})_\n"]
text = "\n".join(out)
open("COMPARISON.md", "w", encoding="utf-8").write(text)
print(text)
