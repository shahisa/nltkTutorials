from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentance = "This is an english showing of stop word filtration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentance)
filteredSentence = []

for w in words:
	if w not in stop_words:
		filteredSentence.append(w)

print (filteredSentence)