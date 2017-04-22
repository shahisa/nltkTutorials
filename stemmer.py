from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

exampleWords = ["python","pythoning","pythoner","pythoned","pythonly"]

#for w in exampleWords:
#	print (ps.stem(w))

exampleText = "It is very important to be pythonly while pythoning because of the danger when seeing a python. Remember while pythoning you must eat a python. That way you can become a good pythoner."

words = word_tokenize(exampleText)
for w in words:
	print (ps.stem(w))