from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBEDDING_MODEL

_model = SentenceTransformer(EMBEDDING_MODEL)

def embed_texts(texts):
    embeddings = _model.encode(texts)
    return embeddings.astype("float32")
