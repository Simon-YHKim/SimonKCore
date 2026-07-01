#!/usr/bin/env python3
"""semantic_index.py - local, zero-API-cost semantic search over the second brain.

L3 layer for SimonK infra (fills the "second brain levels" L3 gap). Builds a vector
index over markdown (Obsidian SimonKWiki vault + .claude memory) using a LOCAL
sentence-transformer, and queries it by meaning. No API cost, offline after first run.

Usage:
    python semantic_index.py build  [--roots PATH ...] [--out DIR]
    python semantic_index.py query  "your question"   [-k 8] [--index DIR]

One-time setup:  pip install sentence-transformers numpy
Model all-MiniLM-L6-v2 (~90MB) auto-downloads on first run, then cached/offline.

Design notes (from the transcript caveats):
  - Vectors are for needle-in-haystack recall ONLY. They miss aggregates/whole-file
    context, so callers must OPEN the source .md for full context (never trust a chunk
    summary). Evergreen summaries stay as markdown.
  - The index is a DERIVED artifact (regenerable), never a system of record.
"""
import argparse
import glob
import json
import os
import re
import sys

DEFAULT_ROOTS = [
    r"C:\Coding Infra\obsidian\SimonKWiki\wiki",
    r"C:\Users\Soha.Bae\.claude\projects\C--Coding-Infra\memory",
]
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_INDEX = os.path.join(HERE, ".semantic-index")
MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_CHARS = 800
CHUNK_OVERLAP = 150


def _load_model():
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError:
        sys.exit("[semantic-recall] Missing dep. Run:  pip install sentence-transformers numpy")
    return SentenceTransformer(MODEL_NAME)


def _np():
    try:
        import numpy as np
    except ImportError:
        sys.exit("[semantic-recall] Missing dep. Run:  pip install numpy")
    return np


def iter_md(roots):
    for root in roots:
        if not os.path.isdir(root):
            print(f"[warn] skip missing root: {root}", file=sys.stderr)
            continue
        for p in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
            yield p


def read_text(path):
    # utf-8 with replacement so Windows cp949 / stray bytes never crash the walk
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def chunk_doc(text):
    """Split by markdown headings, then window long sections. Yields (heading, chunk)."""
    # section boundaries at any heading line
    parts = re.split(r"(?m)^(#{1,6}\s+.*)$", text)
    sections = []
    if parts and parts[0].strip():
        sections.append(("(intro)", parts[0]))
    for i in range(1, len(parts), 2):
        heading = parts[i].lstrip("# ").strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sections.append((heading, body))
    for heading, body in sections:
        body = body.strip()
        if not body:
            continue
        if len(body) <= CHUNK_CHARS:
            yield heading, body
        else:
            start = 0
            while start < len(body):
                yield heading, body[start:start + CHUNK_CHARS]
                start += CHUNK_CHARS - CHUNK_OVERLAP


def build(roots, out):
    np = _np()
    model = _load_model()
    metas, texts = [], []
    for path in iter_md(roots):
        try:
            doc = read_text(path)
        except OSError as e:
            print(f"[warn] read fail {path}: {e}", file=sys.stderr)
            continue
        for heading, chunk in chunk_doc(doc):
            metas.append({"file": path, "heading": heading, "text": chunk})
            texts.append(f"{heading}\n{chunk}")
    if not texts:
        sys.exit("[semantic-recall] no markdown chunks found under the given roots.")
    print(f"[semantic-recall] embedding {len(texts)} chunks from {len(set(m['file'] for m in metas))} files ...")
    emb = model.encode(texts, batch_size=64, show_progress_bar=True, normalize_embeddings=True)
    os.makedirs(out, exist_ok=True)
    np.save(os.path.join(out, "embeddings.npy"), np.asarray(emb, dtype="float32"))
    with open(os.path.join(out, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(metas, f, ensure_ascii=False)
    print(f"[semantic-recall] wrote index -> {out}  ({len(texts)} chunks)")


def query(index, q, k):
    np = _np()
    emb_path = os.path.join(index, "embeddings.npy")
    meta_path = os.path.join(index, "meta.json")
    if not (os.path.exists(emb_path) and os.path.exists(meta_path)):
        sys.exit(f"[semantic-recall] no index at {index}. Run `build` first.")
    emb = np.load(emb_path)
    with open(meta_path, "r", encoding="utf-8") as f:
        metas = json.load(f)
    model = _load_model()
    qv = model.encode([q], normalize_embeddings=True)[0]
    scores = emb @ np.asarray(qv, dtype="float32")
    top = np.argsort(-scores)[:k]
    print(f"\n[semantic-recall] top {k} for: {q}\n")
    for rank, i in enumerate(top, 1):
        m = metas[i]
        snippet = " ".join(m["text"].split())[:180]
        print(f"{rank:2}. {scores[i]:.3f}  {m['file']}  #{m['heading']}")
        print(f"     {snippet}\n")
    print("[note] open the source .md for full context - chunks omit aggregates/whole-file meaning.")


def main():
    ap = argparse.ArgumentParser(description="Local semantic search over the second brain (L3).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="build/refresh the vector index")
    b.add_argument("--roots", nargs="+", default=DEFAULT_ROOTS)
    b.add_argument("--out", default=DEFAULT_INDEX)
    qp = sub.add_parser("query", help="query the index by meaning")
    qp.add_argument("q")
    qp.add_argument("-k", type=int, default=8)
    qp.add_argument("--index", default=DEFAULT_INDEX)
    args = ap.parse_args()
    if args.cmd == "build":
        build(args.roots, args.out)
    elif args.cmd == "query":
        query(args.index, args.q, args.k)


if __name__ == "__main__":
    main()
