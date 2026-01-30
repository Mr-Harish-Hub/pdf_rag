from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBEDDING_MODEL

_model = SentenceTransformer(EMBEDDING_MODEL)

def embed_query(query):
    embedding = _model.encode([query])
    return embedding.astype("float32")
