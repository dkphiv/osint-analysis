from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(texts):
    vectorizer = TfidfVectorizer(max_features=20, stop_words='english')
    X = vectorizer.fit_transform(texts)
    return vectorizer.get_feature_names_out()