from sklearn.metrics import pairwise
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
from tqdm import tqdm 
import load_datasets
import pandas as pd



sbert = None

def get_prediction(X: List[str], X_cadidates: List[List[str]],device="cpu") -> List[List[str]]:
    model = SentenceTransformer("Voicelab/sbert-large-cased-pl", device=device)
    X_embeddings = model.encode(X)
    results = []
    print("Predicting...")
    for x_cand in tqdm(X_cadidates):
        X_cadidates_embeddings = model.encode(x_cand)
        cosine_similarities = pairwise.cosine_similarity(X_embeddings, X_cadidates_embeddings)
        print(cosine_similarities)
        order = list(reversed(np.argsort(cosine_similarities)[0]))
        sorted_result = np.array(x_cand)[np.array(order)]
        results.append(sorted_result)
    return results


if __name__=='__main__':
    X, X_cand, y = load_datasets.load_train()
    result = get_prediction(X, X_cand, device='cuda')
    pd.DataFrame(result)
