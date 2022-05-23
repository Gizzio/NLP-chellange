import gzip
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

random.seed(42)

for dataset in "dev-0", "test-A":
    with gzip.open(f"{dataset}/in.tsv.gz", "rt") as f_in, open(
        f"{dataset}/out.tsv", "w"
    ) as f_out:
        for line in f_in:
            line = line.rstrip("\n").split("\t")
            query = line[0]
            candidates = line[1:]

            vectorizer = TfidfVectorizer()
            query_v = vectorizer.fit_transform([query.replace("[SEP]", " ")])
            candidates_v = vectorizer.transform(candidates)
            similarites = cosine_similarity(query_v, candidates_v)[0]
            candidates_sorted = sorted(
                zip(candidates, similarites), key=lambda x: x[1], reverse=True
            )
            candidates_sorted = [c[0] for c in candidates_sorted]

            candidates = "\t".join(candidates_sorted) + "\n"
            f_out.write(candidates)
