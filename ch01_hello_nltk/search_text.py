#coding:utf-8
from nltk.book import *

#serch word
print '索引，观察前后词'
text1.concordance("monstrous")

print '搜索相近的词'
text1.similar("monstrous")
print 

print '共同的上下文: monstrous, very'
text2.common_contexts(["monstrous", "very"])
print
