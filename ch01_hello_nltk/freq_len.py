from nltk.book import *
V = set(text1)
long_words = [w for w in V if len(w) > 15]
print sorted(long_words)

fdist5 = FreqDist(text5)
print sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])
