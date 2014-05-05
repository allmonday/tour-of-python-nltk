from nltk.book import *
fdist1 = FreqDist(text1)
print fdist1
vocabulary1 = fdist1.keys()
print vocabulary1[:50]
print sum(fdist1.values())
fdist1.plot(50, cumulative=True)

