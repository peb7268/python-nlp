import nltk
from nltk.book import *
import urllib.request
from bs4 import BeautifulSoup



def sum_woody_harrelson():
    print("=== SUMMARIZING WOODY HARRELSON =====")

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
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)
    for key,val in freq.items():
        print(str(key) + ':' + str(val))

    freq.plot(20, cumulative = False)

def sum_genesis():
    print("=== SUMMARIZING GENESIS =====")

    from nltk.corpus import stopwords
    sr = stopwords.words('english')
    tokens = sorted(list(text3))
    clean_tokens = tokens[:]

    for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)
    for key,val in freq.items():
        print(str(key) + ':' + str(val))

    freq.plot(50, cumulative = False)

# sum_woody_harrelson()
sum_genesis()