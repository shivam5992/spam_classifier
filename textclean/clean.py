#-*- coding: utf-8 -*- 
import csv
import re
import fixer
from nltk.corpus import stopwords
import nltk, string
from appos import appos
import HTMLParser, itertools
from BeautifulSoup import UnicodeDammit

html_parser = HTMLParser.HTMLParser()
exclude = set(string.punctuation)
	
def appos_look_up(text):
	words = text.split()
	new_text = []
	for word in words:
		word_s = word.lower()
		if word_s in appos.appos:
			new_text.append(appos.appos[word_s])
		else:
			new_text.append(word)
	apposed = " ".join(new_text)
	apposed = apposed.replace("'s", "")

	return apposed

def remove_expressions(text):
	newtext = text
	if text.find("[") >= 0:
		indexes = [m.start() for m in re.finditer('\[', text)]
		for ind in indexes:
			indf = text[ind:].find("]")
			newtext = newtext.replace(text[ind:ind + indf] + "]", " ")
	text = newtext.replace("—","  ")
	return text

def handle_encoding(text):
	text = text.decode("utf-8")
	text = fixer.fix_bad_unicode(text)
	return text

def remove_punctuations(text, customlist):
	if not customlist:
		customlist = exclude
	for punc in customlist:
		text = text.replace(punc, " ")
	return text

def remove_stopwords(text):
	tokenized_words = text.split()
	filtered_words = []
	for word in tokenized_words:
		if not word.lower() in stopwords.words('english'):
			filtered_words.append(word)
	text = " ".join(filtered_words)
	return text

def extra_rep(text):
	for each in exclude:
		text = text.replace(each+each, each)
		text = text.lstrip(each).rstrip(each)
	text = re.sub(' +',' ',text)
	text = text.strip()
	return text

def improve_repeated(text):
	text = ''.join(''.join(s)[:2] for _, s in itertools.groupby(text))
	return text 

def escape(text):
    return html_parser.unescape(text)

def more_replace(text):
	text = text.replace("- ", "")
	text = text.replace(" - ", "")
	text = text.replace('(cid:129)',"")
	return text

def super_clean(text):
	dammit = UnicodeDammit(text)
	cdata = dammit.unicode_markup
	cdata = cdata.encode('utf-8')
	return cdata 

def remove_numeric(text):
	text = re.sub("\d", " ", text)
	text = re.sub(' +',' ',text)
	return text