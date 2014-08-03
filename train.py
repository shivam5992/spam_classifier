from utility import utility
import glob, json

class trainer():

	def __init__(self, textdata):
		self.message = textdata
		return None

	def _trainwords(self, text):
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

	def _create_unique_word_bag(self,text):
		words = list(set(text.split()))
		return words



if __name__ == '__main__':
	use = utility()
	overall_spam = {}
	for index, eachfile in enumerate(glob.glob('training_data/SPAM_DATA/*.spam.txt')):		
		print index
		if index <= 13200: # spam
		#if index <= 13236: # ham
			try:
				data = open(eachfile).read()
				train = trainer(data)
				message = use._cleantext(data)
				itsporb = train._create_unique_word_bag(message)
				for x in itsporb:
					if x in overall_spam:
						overall_spam[x] += 1
					else:
						overall_spam[x] = 1

				# pickle_bigram = train._traingram(message, 3)
				# for key, value in pickle_bigram['bag'].iteritems():
				# 	if key in bigram_dump:
				# 		bigram_dump[key] += value
				# 	else:
				# 		bigram_dump[key] = value

			except:
			 	continue
		
	use._dumppickle(overall_spam, "SPAM_Learnt_Data")