#coding=utf-8
import nltk
from nltk.corpus import brown


print brown.categories()

'''打印新闻类文本特定词汇出现频次'''
news_text = brown.words(categories="news")
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can',  'could', 'may', 'might', 'must', 'will']
for m in modals:
    print m + ':' , fdist[m]

'''better way~'''
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories = genre)
        )
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance' , 'humor']
print cfd.tabulate(conditions= genres, samples = modals)
