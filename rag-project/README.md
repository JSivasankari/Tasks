# RAG over a Security Policy Handbook

A from-scratch Retrieval-Augmented Generation system: **Chroma** (local vector DB) + **Gemini** (LLM).
It answers questions from a private document set that no public LLM has seen.

## Document set
`data/` holds 5 markdown files (~4,000 words) of the fictional **Nimbus Labs** security handbook
(incident response, access control, vulnerability management, data handling, people policies).
The facts are invented (tool names, SLAs, numbers), so a plain LLM *cannot* know them.
Swap in your own `.md` files to use any corpus.

## How it works
1. `chunker.py` – paragraph-aware chunks of ~300 words (~400 tokens) with 50-word overlap
2. `ingest.py` – embeds chunks (Chroma default: all-MiniLM-L6-v2, local) and stores them
3. `retrieve.py` – embeds the question, returns top-4 chunks by cosine distance
4. `rag.py` – injects chunks into the prompt; model must answer only from context and cite sources
5. `compare.py` – asks the same questions with and without retrieval

## Run
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # add your free key from aistudio.google.com
python src/chunker.py       # inspect chunks
python src/ingest.py        # build the vector DB
python src/retrieve.py "What is the war room voice bridge called?"   # check retrieval
python src/rag.py "What is the max bug bounty reward?"
python src/compare.py       # writes COMPARISON.md
```

## With RAG vs. without RAG
Run `python src/compare.py` and paste the contents of `COMPARISON.md` here as evidence.
Expected: without RAG the model says it doesn't know or guesses; with RAG it answers
correctly (e.g. voice bridge **Beacon-7**, KeyKeeper max **4 hours**, bounty up to **USD 7,500**,
critical fix in **72 hours**, scanner **Sextant**) and cites the source file.
