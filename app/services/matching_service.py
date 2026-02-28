from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similar(new_item, existing_items, min_score=0.0):
    """Return cosine similarity scores between the new_item and each item in existing_items.

    A minimum score can be provided; callers may ignore scores below that threshold.
    """
    if not existing_items:
        # nothing to compare against
        return []

    corpus = [new_item] + existing_items
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(vectors[0:1], vectors[1:])
    scores = similarity.tolist()[0]
    if min_score > 0:
        # filter results in place by threshold
        scores = [s if s >= min_score else 0.0 for s in scores]
    return scores