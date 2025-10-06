from sklearn.feature_extraction.text import CountVectorizer


texts = ["Data science is fun", "Machine learning is amazing"]
vectorizer = CountVectorizer()
bow = vectorizer.fit_transform(texts)


print("Feature Names:", vectorizer.get_feature_names_out())
print("BoW Representation:\n", bow.toarray())
