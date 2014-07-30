from textclean import clean
import json, glob
import numpy as np

class naiveBayesClassifier():
	def __init__(self, spam_pickle, ham_pickle):
		self.SPAMWORD = json.loads(open(spam_pickle).read())
		self.HAMWORD = json.loads(open(ham_pickle).read())

	def _cleantext(self, text):
		text = text.replace("Subject", "")
		text = clean.handle_encoding(text)
		text = clean.escape(text)
		text = clean.appos_look_up(text)
		text = clean.extra_rep(text)
		text = clean.improve_repeated(text)
		text = clean.remove_punctuations(text, [])
		text = clean.remove_stopwords(text)
		text = clean.remove_numeric(text)
		return text

	def _classify(self, message, spam_total, ham_total):
		problist = []
		probS = float(spam_total)/(ham_total+spam_total) 
		probH = float(ham_total)/(ham_total+spam_total)
		wordlist = message.split()
		aterm, bterm = 0 , 0
		flag = 0
		for eachword in wordlist:
			if eachword in self.SPAMWORD:
				if eachword in self.HAMWORD:
					WnS = float(self.SPAMWORD[eachword])/ spam_total
					WnH = float(self.HAMWORD[eachword])/ ham_total
					SnW = WnS/(WnS + WnH)
					SnW = round(SnW, 3)
					aterm += np.log(1 - SnW)
					bterm += np.log(SnW)
					flag = 1
		if flag == 1:
			cterm = aterm - bterm
			return 1/(np.exp(cterm) + 1)
		else:
			return 0

if __name__ == '__main__':	
	naivebayes = naiveBayesClassifier('pickle_wordspam.json', 'pickle_wordham.json')
	threshold = 0
	i = 0
	for filename in glob.glob("training_data/spam/*.txt"):
		email = open(filename).read()
		message = naivebayes._cleantext(email)
		spamicity = naivebayes._classify(message, spam_total = 1500, ham_total = 3692)
		print spamicity

