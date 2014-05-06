import nltk
from nltk.corpus import udhr

languages = ['Chickasaw', 'English','German_Deutsch']
cfd  =nltk.ConditionalFreqDist(
        (lang, len(word))
        for lang in languages
        for word in udhr.words(lang + '-Latin1')
        )
cfd.plot(cumulative= True)
