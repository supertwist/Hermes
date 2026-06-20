import os, json
from pathlib import Path
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import re

def load_chunks(base_dir: str, chunk_size: int = 2000):
    """Return list of (rel_path, text_chunk)."""
    chunks = []
    for root, _, files in os.walk(base_dir):
        for f in files:
            if not f.lower().endswith('.txt'):
                continue
            full_path = Path(root) / f
            rel_path = str(full_path.relative_to(base_dir))
            try:
                text = full_path.read_text(encoding='utf-8', errors='ignore')
            except Exception:
                continue
            # Normalise whitespace
            text = re.sub(r'\s+', ' ', text).strip()
            for i in range(0, len(text), chunk_size):
                chunk = text[i:i+chunk_size].strip()
                if chunk:
                    chunks.append((rel_path, chunk))
    return chunks

def build_index(chunks, embed_model):
    texts = [c[1] for c in chunks]
    embeddings = embed_model.encode(texts, normalize_embeddings=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # inner product works with normalized vectors -> cosine similarity
    index.add(np.asarray(embeddings).astype('float32'))
    return index, embeddings

def main():
    base_dir = os.path.expanduser('~/GIT/Hermes/OSSI/demo/rhino_docs')
    chunks = load_chunks(base_dir)
    if not chunks:
        print('No text chunks found under', base_dir)
        return
    model = SentenceTransformer('all-MiniLM-L6-v2')
    index, _ = build_index(chunks, model)
    # Save index and mapping
    save_dir = os.path.expanduser('~/.hermes/rag/rhino8')
    os.makedirs(save_dir, exist_ok=True)
    faiss.write_index(index, os.path.join(save_dir, 'index.faiss'))
    with open(os.path.join(save_dir, 'chunks.json'), 'w', encoding='utf-8') as f:
        json.dump(chunks, f)
    print(f'Built FAISS index with {len(chunks)} chunks; saved to {save_dir}')

if __name__ == '__main__':
    main()
