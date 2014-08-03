#Bayesian spam filtering


Bayesian spam filtering is a technique based on statistics for of e-mail classification. It is in general a naive Bayes classifier on lexicon lookup table with lexicons as features to identify spam e-mail.

###Training of Spam and Ham pickle

This classifier makes use of public dataset released by Enron Corporation. With over 17000 Spam mails and 15000 Ham mails, enron corpus is trained by Navive Bayes Classifier. The pivot feature of this approach is the words. Bag of words is created with frequency distibution of them in ham and spam mails. The trained dump is stored in a pickle file.

###Spamicity

Spamicity is calculated using bayesian forumla
	 
	prob_SnW = prob_WnS/(prob_WnS + prob_WnH)
	
	prob_SnW = P(Spam/Word)
	prob_Wns = P(Word/Spam)
	prob_WnH = P(Word/Ham)
	
This term is the calculated for each word in the test mail. The combined probability is calculated using this formula:
	
	X = SUMMATION[log(1 - prob_SnW)]
	Y = SUMMATION[log(prob_SnW)]
	Spamicity = 1/(EXP(X-Y) + 1)

Average spamicity trained on 80% of SPAM test data gives value of 0.9.

Average hamicity trained on 80% of HAM test data gives value of 0.09.

###Classfication

Spamicity for Test mail is calculated. If its less than 0.5 then is more probably a HAM mail, else SPAM mail.

Training Data can be downloaded from <a href="https://www.cs.cmu.edu/~./enron/">Here</a>.
