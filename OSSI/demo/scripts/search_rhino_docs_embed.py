import os, json, re
from pathlib import Path
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

def _load_index():
    base = os.path.expanduser('~/.hermes/rag/rhino8')
    index_path = os.path.join(base, 'index.faiss')
    chunks_path = os.path.join(base, 'chunks.json')
    if not os.path.exists(index_path) or not os.path.exists(chunks_path):
        raise FileNotFoundError('FAISS index or chunks missing – run build_rhino_rag.py first.')
    index = faiss.read_index(index_path)
    with open(chunks_path, 'r', encoding='utf-8') as f:
        chunks = json.load(f)  # list of (rel_path, chunk_text)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return index, model, chunks

def search(query: str, top_k: int = 3) -> str:
    idx, model, chunks = _load_index()
    q_vec = model.encode([query], normalize_embeddings=True).astype('float32')
    distances, ids = idx.search(q_vec, top_k)
    results = []
    for rank, (dist, i) in enumerate(zip(distances[0], ids[0])):
        if i < 0 or i >= len(chunks):
            continue
        rel_path, chunk = chunks[i]
        score = float(dist)
        snippet = chunk.strip()[:500].replace('\n', ' ')
        results.append(f"[{rank+1}] ({rel_path}) – similarity {score:.4f}\n{snippet}…")
    if not results:
        return "No relevant documentation found."
    return "\n\n".join(results)

if __name__ == '__main__':
    import sys
    query = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else ''
    print(search(query))
