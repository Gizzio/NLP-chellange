from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import load_datasets
import torch
from random import choice
from typing import List
from tqdm import tqdm
from sklearn.metrics import pairwise
import numpy as np
import pandas as pd


def get_prediction(X: List[str], X_cadidates: List[List[str]], model) -> List[List[str]]:
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

#Define the model. Either from scratch of by loading a pre-trained model
model = SentenceTransformer("Voicelab/sbert-base-cased-pl", device="cuda")

#Define your train examples. You need more than just two examples...
X, X_cand, y = load_datasets.load_train()

# pozytywne example
positives = list(zip(X, y))

# po jednym negatywnym
y_wrong = []
for gt, cand in zip(y, X_cand):
    y_false = choice(cand)
    if y_false == gt:
        y_false = choice(cand)

    y_wrong.append(y_false)

negatives = list(zip(X, y_wrong))

train_examples = []

for ex in positives:
    train_examples.append(InputExample(texts=ex, label=1.0))

for ex in negatives:
    train_examples.append(InputExample(texts=ex, label=0.0))

# train_examples = choice()


# train_examples = [InputExample(texts=['My first sentence', 'My second sentence'], label=0.8),
#     InputExample(texts=['Another pair', 'Unrelated sentence'], label=0.3)]

#Define your train dataset, the dataloader and the train loss
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=32)
train_loss = losses.ContrastiveLoss(model)

#Tune the model
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=5, warmup_steps=100)
print("Saving...")
torch.save(model.state_dict(), "siamese_model.pth")

result = get_prediction(X, X_cand, model)
df = pd.DataFrame(result)
df.to_csv("siamese_train_result.tsv", sep='\t', index=False, header=False)

X_test, X_cand_test = load_datasets.load_test()

result = get_prediction(X_test, X_cand_test,  model)
df = pd.DataFrame(result)
df.to_csv("siamese_test_result.tsv", sep='\t', index=False, header=False)