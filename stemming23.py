from nltk.stem import PorterStemmer


ps = PorterStemmer()
words = ['running', 'runs', 'runner', 'easily', 'fairly']
stemmed_words = [ps.stem(word) for word in words]
print("Set of words:",words)
print("Stemmed Words:", stemmed_words)