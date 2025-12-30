import nltk
from nltk.stem import WordNetLemmatizer

# Download required data (run once)
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

# User input
words = input("Enter words separated by spaces: ").split()

print("\nMorphological Analysis:")
for word in words:
    lemma = lemmatizer.lemmatize(word)
    print(f"{word} -> {lemma}")
