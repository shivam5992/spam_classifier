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
	# word_dump = {}
	# bigram_dump = {}
	# trigram_dump = {}

	overall_spam = {}
	for index, eachfile in enumerate(glob.glob('training_data/ham/*.txt')):		
		print index
		try:
			data = open(eachfile).read()
			train = trainer(data)
			use = utility()
			message = use._cleantext(data)
			itsporb = train._create_unique_word_bag(message)
			for x in itsporb:
				if x in overall_spam:
					overall_spam[x] += 1
				else:
					overall_spam[x] = 1

			# pickle_words = train._trainwords(message)
			# for key, value in pickle_words.iteritems():
			# 	if key in word_dump:
			# 		word_dump[key] += value
			# 	else:
			# 		word_dump[key] = value

			# pickle_bigram = train._traingram(message, 2)
			# for key, value in pickle_bigram['bag'].iteritems():
			# 	if key in bigram_dump:
			# 		bigram_dump[key] += value
			# 	else:
			# 		bigram_dump[key] = value

			# pickle_trigram = train._traingram(message, 3)
			# for key, value in pickle_trigram['bag'].iteritems():
			# 	if key in trigram_dump:
			# 		trigram_dump[key] += value
			# 	else:
			# 		trigram_dump[key] = value

		except:
		 	continue
		
	# use = utility()
	# use._dumppickle(word_dump, "word")
	# use._dumppickle(bigram_dump, "bigram")
	# use._dumppickle(trigram_dump, "trigram")
	use._dumppickle(overall_spam, "word_prob_base")

