import nltk 
from nltk.book import *

f = open ('wordlist.txt','rU')
text = f.read()
text1 = text.split()
abstracts = nltk.Text(text1)

abstracts.concordance("rhetoric")