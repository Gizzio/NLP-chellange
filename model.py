from transformers import AutoTokenizer, AutoModel
from sklearn.metrics import pairwise
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

model = SentenceTransformer("Voicelab/sbert-large-cased-pl")


def get_prediction(X: List[str], X_cadidates: List[List[str]]) -> List[List[str]]:
    X_embeddings = model.encode(X)
    results = []
    for x_cand in X_cadidates:
        X_cadidates_embeddings = model.encode(x_cand)
        cosine_similarities = pairwise.cosine_similarity(X_embeddings, X_cadidates_embeddings)
        print(cosine_similarities)
        order = np.argsort(cosine_similarities)
        sorted_result = x_cand[order]
        results.append(sorted_result)
    return results