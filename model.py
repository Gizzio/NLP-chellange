from sklearn.metrics import pairwise
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
from tqdm import tqdm 
import load_datasets
import pandas as pd

import typer
from enum import Enum


class Dataset(str,Enum):
    dev = "dev"
    test = "test"
    train = "train"


sbert = None

def get_prediction(X: List[str], X_cadidates: List[List[str]],device="cpu") -> List[List[str]]:
    print("Loading model...")
    model = SentenceTransformer("Voicelab/sbert-large-cased-pl", device=device)
    X_embeddings = model.encode(X)
    results = []
    print("Predicting...")
    for x_cand in tqdm(X_cadidates):
        X_cadidates_embeddings = model.encode(x_cand)
        cosine_similarities = pairwise.cosine_similarity(X_embeddings, X_cadidates_embeddings)
        order = list(reversed(np.argsort(cosine_similarities)[0]))
        sorted_result = np.array(x_cand)[np.array(order)]
        results.append(sorted_result)
    return results

def main(dataset:Dataset=Dataset.train):
    print("Loading data...")
    if dataset == Dataset.train:
        X, X_cadidates, y = load_datasets.load_train()
    elif dataset == Dataset.dev:
        X, X_cadidates, y = load_datasets.load_dev()
    elif dataset == Dataset.test:
        X, X_cadidates, y = load_datasets.load_test()
    else:
        raise ValueError("Unknown dataset")
    result = get_prediction(X, X_cadidates, device='cuda')
    print("Saving results...")
    df = pd.DataFrame(result)
    df.to_csv(f"sbert_result_{dataset}.tsv",sep='\t', index=False, header=False)


if __name__=='__main__':
    typer.run(main)
