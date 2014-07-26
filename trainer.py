from config import *
from textclean import clean
import glob, json

class utility():

	def __init__(self):
		return None

	def calculate_ngram(self, text, n):
		text = "<s> " + text + " </s>"
		words = text.split()
		ngramlist = []
		for ind in range(len(words)):
			ngramlist.append(" ".join(words[ind : ind + n]))
		return ngramlist

	def _dumppickle(self, dump, name):
		json_encoded = json.dumps(dump)
		outfile = open('pickle_' + name + '.json', 'w')
		outfile.write(json_encoded)
		outfile.close()
		print "Successfully created pickle file of " + name
 		return None

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





if __name__ == '__main__':
	word_dump = {}
	bigram_dump = {}
	trigram_dump = {}
	for index, eachfile in enumerate(glob.glob(TRANING_DATA_SOURCE + "/*.txt")):
		try:
			print index
			data = open(eachfile).read()
			train = trainer(data)
			use = utility()
			message = use._cleantext()

			pickle_words = train._trainwords(message)
			for key, value in pickle_words.iteritems():
				if key in word_dump:
					word_dump[key] += value
				else:
					word_dump[key] = value

			pickle_bigram = train._traingram(message, 2)
			for key, value in pickle_bigram['bag'].iteritems():
				if key in bigram_dump:
					bigram_dump[key] += value
				else:
					bigram_dump[key] = value

			pickle_trigram = train._traingram(message, 3)
			for key, value in pickle_trigram['bag'].iteritems():
				if key in trigram_dump:
					trigram_dump[key] += value
				else:
					trigram_dump[key] = value

		except:
		 	continue
		
	# use = utility()
	# use._dumppickle(word_dump, "word")
	# use._dumppickle(bigram_dump, "bigram")
	# use._dumppickle(trigram_dump, "trigram")

