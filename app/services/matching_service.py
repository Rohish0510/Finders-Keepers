from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similar(new_item, existing_items):
    corpus = [new_item] + existing_items
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(vectors[0:1], vectors[1:])
    return similarity.tolist()[0]