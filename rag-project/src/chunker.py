import re

def chunk_text(text, size=300, overlap=50):
    """Paragraph-aware chunks of ~size words (~400 tokens) with word overlap."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, cur = [], []
    for p in paras:
        words = p.split()
        if cur and len(cur) + len(words) > size:
            chunks.append(" ".join(cur))
            cur = cur[-overlap:]  # carry overlap into next chunk
        cur += words
    if cur:
        chunks.append(" ".join(cur))
    return chunks

if __name__ == "__main__":  # inspect chunks manually
    import glob
    for f in sorted(glob.glob("data/*.md"))[:1]:
        for i, c in enumerate(chunk_text(open(f, encoding="utf-8").read())):
            print(f"--- chunk {i} ({len(c.split())} words) ---\n{c[:250]}...\n...{c[-150:]}\n")
