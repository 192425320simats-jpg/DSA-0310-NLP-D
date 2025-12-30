import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, BigramTagger

nltk.download('treebank')
nltk.download('universal_tagset')

train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]

unigram_tagger = UnigramTagger(train_sents)
bigram_tagger = BigramTagger(train_sents, backoff=unigram_tagger)

print("Unigram Tagger Accuracy: ", unigram_tagger.evaluate(test_sents))
print("Bigram Tagger Accuracy: ", bigram_tagger.evaluate(test_sents))

sentence = "The quick brown fox jumped over the lazy dog".split()
tags = bigram_tagger.tag(sentence)
print(tags)
