#coding:utf-8
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, ".*")
print wordlists.fileids()
print wordlists.words('american-english')
#for w in wordlists.words('china'):
#    print w.decode('ascii')      #output error
