import os
from dotenv import load_dotenv
from google import genai
from retrieve import retrieve

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash"

def _llm(prompt):
    return client.models.generate_content(model=MODEL, contents=prompt).text.strip()

def plain(question):
    """No retrieval: the model answers from its own knowledge only."""
    return _llm(question)

def rag(question, k=4):
    hits = retrieve(question, k)
    context = "\n\n".join(f"[{h['source']}]\n{h['text']}" for h in hits)
    prompt = (
        "Answer using ONLY the context below. If the answer is not in the context, "
        "say you don't know. Cite the source file names.\n\n"
        f"CONTEXT:\n{context}\n\nQUESTION: {question}"
    )
    return _llm(prompt), hits

if __name__ == "__main__":
    import sys
    q = " ".join(sys.argv[1:]) or "What is the SEV-1 acknowledgement time?"
    print(rag(q)[0])
