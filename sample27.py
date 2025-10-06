import nltk
import re
from nltk.corpus import stopwords
from num2words import num2words


# Download stopwords
nltk.download('stopwords')


# Sample text
with open('sample.txt') as file:  # Make sure you have a file named 'sample_text.txt'
   text = file.read()


print("Original Text:", text)


# 1. Convert to lowercase
text_lower = text.lower()
print("Lowered Text:", text_lower)


# 3. Remove numbers
text2 = re.sub(r'\d+', '', text)
print("After Removing Numbers:", text2)


# 2. Convert numbers to words
text_num_words = re.sub(r'\d+', lambda x: num2words(int(x.group())), text)
print("Numbers Converted to Words:", text_num_words)


# 3. Remove punctuation
text_no_punct = re.sub(r'[^\w\s]', '', text)
print("After Removing Punctuation:", text_no_punct)


# 4. Remove extra whitespace
text_clean = re.sub(r'\s+', ' ', text).strip()
print("After Removing Extra Whitespace:", text_clean)


# 5. Remove stopwords
stop_words = set(stopwords.words('english'))
words = text.split()
words_no_stopwords = [word for word in words if word not in stop_words]
text_no_stopwords = ' '.join(words_no_stopwords)
print("After Removing Stopwords:", text_no_stopwords)
