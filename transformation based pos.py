import nltk
from nltk.corpus import treebank
from nltk.tag import DefaultTagger
from nltk.tag import tnt

nltk.download('treebank')

train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]

default_tagger = DefaultTagger('NN')

tnt_tagger = tnt.TnT()
tnt_tagger.train(train_sents)

print("TnT Tagger Accuracy: ", tnt_tagger.evaluate(test_sents))

sentence = "The quick brown fox jumped over the lazy dog".split()
tags = tnt_tagger.tag(sentence)
print(tags)
