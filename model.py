from transformers import AutoTokenizer, AutoModel
from sklearn.metrics import pairwise
from sentence_transformers import SentenceTransformer
from typing import List


model = SentenceTransformer("Voicelab/sbert-large-cased-pl")


def get_prediction(X: List[str], X_cadidates: List[List[str]]) -> List[List[str]]:
    X_embeddings = model.encode(X)
    X_cadidates_embeddings = model.encode(X_cadidates)
