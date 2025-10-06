from sklearn.feature_extraction.text import TfidfVectorizer


texts = ["Data science is fun", "Machine learning is amazing"]
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(texts)


print("Feature Names:", tfidf.get_feature_names_out())
print("TF-IDF Representation:\n", tfidf_matrix.toarray())