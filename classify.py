from textclean import clean
from utility import utility
import json, glob
import numpy as np

class naiveBayesClassifier():
	def __init__(self, spam_pickle, ham_pickle):
		self.SPAMWORD = json.loads(open('pickle/' + spam_pickle).read())
		self.HAMWORD = json.loads(open('pickle/' + ham_pickle).read())

	def _classify(self, message, spam_total, ham_total):
		problist = []
		probS = float(spam_total)/(ham_total+spam_total) 
		probH = float(ham_total)/(ham_total+spam_total)
		wordlist = message.split()
		aterm, bterm = 0 , 0
		isImportant = False
		for eachword in wordlist:
			if eachword in self.SPAMWORD:
				if eachword in self.HAMWORD:
					prob_WnS = float(self.SPAMWORD[eachword])/ spam_total
					prob_WnH = float(self.HAMWORD[eachword])/ ham_total
					prob_SnW = prob_WnS/(prob_WnS + prob_WnH)
					prob_SnW = round(prob_SnW, 3)
					aterm += np.log(1 - prob_SnW)
					bterm += np.log(prob_SnW)
					isImportant = True
		if isImportant:
			cterm = aterm - bterm
			return 1/(np.exp(cterm) + 1)
		else:
			return 0

if __name__ == '__main__':	
	naivebayes = naiveBayesClassifier('pickle_wordspam.json', 'pickle_wordham.json')
	sum_spamicity = 0
	count = 1
	for filename in glob.glob("training_data/ham/*.txt"):
		try:
			email = open(filename).read()
			message = utility()._cleantext(email)
			spamicity = naivebayes._classify(message, spam_total = 1500, ham_total = 3692)
			print count
			count += 1
			## Decide Threshold		
			sum_spamicity += spamicity
		except:
			continue
	print float(sum_spamicity)/3692
	#SPAM_VAL = 0.956258890514
	#HAM_VAL = 0.0927524323055

