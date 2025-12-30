import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')

stemmer = PorterStemmer()

words = ["running", "runner", "easily", "happiness", "cats", "flying", "tried", "studies"]

stems = [stemmer.stem(word) for word in words]

for word, stem in zip(words, stems):
    print(f"Original: {word} → Stemmed: {stem}")
