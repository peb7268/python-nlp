#NLRP - natural language processing

import nltk
from nltk.book import *
import urllib.request
from bs4 import BeautifulSoup

#texts() lists texts
#text3 genesis
#text7 wall st journal

### Searching for occurrances in a text
text3.concordance("day");

### Searching for similar items
text3.similar("let");

### Comparing the context shared by two or more words
text3.common_contexts(["day", "night"])

### Seeing the length of text
len(text3)  #44764


"""
A token is a set of characters that we want to treat as a group.
The vocabulary of a text is just the set of tokens that it contains.
In a set, all duplicates are collapsed todether.
"""

### Obtaining the vocabulary items of a text
set(text3)
len(sorted(set(text3))) #2789 distinct words

### Reading text from a webpage
response = urllib.request.urlopen("https://en.wikipedia.org/wiki/Woody%20Harrelson")
html = response.read()
print(html)

soup = BeautifulSoup(html, 'html5lib')  #clean up and parse the contents
text = soup.get_text(strip = True)
print(text)

### Tokenize the text
tokens = [t for t in text.split()]
print(tokens)

### Count word frequency
from nltk.corpus import stopwords
sr = stopwords.words('english')
clean_tokens = tokens[:]

for token in tokens:
    if token in stopwords.words('english')
        clean_tokens.remove(token)


