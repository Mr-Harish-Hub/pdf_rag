from ingestion.pdf_loader import load_pdf
import os
from ingestion.cleaner import clean_text
from ingestion.chunker import chunk_text
from ingestion.embedder import embed_texts
from ingestion.indexer import build_faiss_index
from retrieval.query_embedder import embed_query
from retrieval.retriever import retrieve_dynamic_chunks

from llm.generator import generate_answer
from config import CHUNK_SIZE, CHUNK_OVERLAP, TOP_K


PDF_PATH = input("\nEnter PDF file path: ").strip()
QUESTION = input("\nEnter your question: ")






pages = load_pdf(PDF_PATH)

chunks = []
for page in pages:
    cleaned = clean_text(page["text"])
    chunks.extend(chunk_text(cleaned, CHUNK_SIZE, CHUNK_OVERLAP))

embeddings = embed_texts(chunks)
index = build_faiss_index(embeddings)
print("ingestion completed")

query_embedding = embed_query(QUESTION)
top_chunks = retrieve_dynamic_chunks(
    query_embedding=query_embedding,
    index=index,
    chunks=chunks,
    max_k=10,
    distance_threshold=1.2
)
print("embedding Completed")

context = "\n".join([c["chunk"] for c in top_chunks])

answer = generate_answer(context, QUESTION)
print(answer)

