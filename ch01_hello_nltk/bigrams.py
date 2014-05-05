from nltk.book import *

print bigrams(['more', 'is', 'said','than','done'])
'''>>>[('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')] '''

print text4.collocations()
print text1.collocations()
