import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
# Sample text
text = "Data science is fun and exciting!"
# Tokenization
tokens = word_tokenize(text)
print("Orginal:",text)
print("Tokens:", tokens)
