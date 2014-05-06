import nltk
#print nltk.corpus.gutenberg.fileids()
print 'loading emma'
#emma = nltk.corpus.gutenberg.words('austen-emma.txt')
#print len(emma)

#wrap to use concordance, it would look like nltk.book's behavior
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt')) 
print emma.concordance("taken")


