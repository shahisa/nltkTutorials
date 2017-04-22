from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords



# tokenizing - word tokenizers ... sentence tokenizers
#lexicon and corporas
# corpora - body of text. ex: medical journals, presidential speeches, English language
#lexicon - words and their meanings
# investor-speak ... regular - english-speach

#investor speach 'bull' - someone who is positive about the market
# english-speach 'bull' - scary horned animal that chases huans.


example_text = "Hello Mr.Abul, there how are you today? The weather is great and python is awesome! The sky is pinkish-blue you should not eat" \
               "cardboard. "
#print(sent_tokenize(example_text))

#print(word_tokenize(example_text))

#for i in word_tokenize(example_text):
#    print(i)

exampleSentence = "This is an example showing off stopword filtration."
stopWords = set(stopwords.words("english"))

words = word_tokenize(exampleSentence)

filteredSentence = []

for w in words:
    if w not in stopWords:
        filteredSentence.append(w)

print(filteredSentence)
