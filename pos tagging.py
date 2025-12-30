import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "NLTK is a leading platform for building Python programs to work with human language data."

tokens = word_tokenize(text)

tagged_words = nltk.pos_tag(tokens)

print("Part-of-Speech Tagged Words:")
print(tagged_words)
