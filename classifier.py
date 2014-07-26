import json
from trainer import utility, trainer
WORD = json.loads(open('pickle_word.json').read())
BIGRAM = json.loads(open('pickle_bigram.json').read())
TRIGRAM = json.loads(open('pickle_trigram.json').read())


class classify():

	def __init__(self, textdata):
		self.message = textdata
		return None

	def _classify(self):
		text = self.message

		words = text.split()
		bag_of_words = {}
		for word in words:
			if word not in bag_of_words:
				bag_of_words[word] = 1
			else:
				bag_of_words[word] += 1
		return bag_of_words

	def _traingram(self, text, n):
		grams = utility().calculate_ngram(text, n)
		bag_of_ngrams = {'ngram' : n, 'bag' : {} }
		for wordcomb in grams:
			if wordcomb not in bag_of_ngrams:
				bag_of_ngrams['bag'][wordcomb] = 1
			else:
				bag_of_ngrams['bag'][wordcomb] += 1
		return bag_of_ngrams

text = open("training_data/ham/0020.1999-12-15.farmer.ham.txt").read()
use = utility()
message = use._cleantext(text)
total = len(message.split())
obj = classify(message)
w = obj._classify()
b = obj._traingram(message , 2)
t = obj._traingram(message , 3)

for k, v in w.iteritems():
	if k in WORD:
		print k
		tf = float(v)
		idf = float(WORD[k])
		print tf/idf
		print

# for k, v in b['bag'].iteritems():
# 	if k in BIGRAM:
# 		print k, v, BIGRAM[k]

# for k, v in t['bag'].iteritems():
# 	if k in TRIGRAM:
# 		print k, v, TRIGRAM[k]