from textclean import clean
from utility import utility
import json, glob
import numpy as np

class naiveBayesClassifier():
	def __init__(self, spam_pickle, ham_pickle, spam_total, ham_total):
		self.SPAMWORD = json.loads(open('pickle/' + spam_pickle).read())
		self.HAMWORD = json.loads(open('pickle/' + ham_pickle).read())
		self.spam_total = spam_total
		self.ham_total = ham_total

	def calculate_spamicity(self, message):
		problist = []
		probS = float(self.spam_total)/(self.ham_total+self.spam_total) 
		probH = float(self.ham_total)/(self.ham_total+self.spam_total)
		wordlist = message.split()
		aterm, bterm = 0 , 0
		isImportant = False
		for eachword in wordlist:
			if eachword in self.SPAMWORD:
				if eachword in self.HAMWORD:
					prob_WnS = float(self.SPAMWORD[eachword])/ self.spam_total
					prob_WnH = float(self.HAMWORD[eachword])/ self.ham_total
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

class train_by_classify():
	def __init__(self):
		return None

	def decide_threshold(self):	
		naivebayes = naiveBayesClassifier('pickle_wordspam.json', 'pickle_wordham.json', spam_total = 1500, ham_total = 3692)
		sum_spamicity = 0
		sum_hamicity = 0
		for count, filename in enumerate(glob.glob("training_data/ham/*.txt")):
			try:
				print count
				email = open(filename).read()
				message = utility()._cleantext(email)
				spamicity = naivebayes.calculate_spamicity(message)
				sum_spamicity += spamicity

				hamicity = naivebayes.calculate_spamicity(message)
				sum_hamicity += hamicity
			except:
				continue
		HAM_VAL = float(sum_hamicity) / ham_total
		SPAM_VAL = float(sum_spamicity) / spam_total
		#SPAM_VAL = 0.956258890514
		#HAM_VAL = 0.0927524323055
		
if __name__ == '__main__':
	tbc = train_by_classify()
	tbcl.decide_threshold()

