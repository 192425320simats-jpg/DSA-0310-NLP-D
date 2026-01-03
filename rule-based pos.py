import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')

text = "The quick brown fox jumped over the lazy dog"
tokens = word_tokenize(text)

patterns = [
    (r'^[A-Z].*', 'NNP'),
    (r'\b(the|a|an)\b', 'DT'),
    (r'\b(jumped|ran|walked)\b', 'VBD'),
    (r'\b(quick|lazy|brown)\b', 'JJ'),
    (r'\b(fox|dog)\b', 'NN'),
    (r'\b(over|under|on|in)\b', 'IN'),
    (r'\b(\d+)\b', 'CD')
]

tagger = RegexpTagger(patterns)
tagged = tagger.tag(tokens)
print(tagged)
