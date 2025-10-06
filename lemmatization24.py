import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()
words = ['runs', 'runner', 'better', 'geese', 'cats', 'mice', 'feet']
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("Set of words: ", words)
print("Lemmatized Words:", lemmatized_words)

