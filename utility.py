from textclean import clean
import json

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