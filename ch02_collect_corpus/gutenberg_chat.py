from nltk.corpus import webtext
from nltk.corpus import nps_chat


for fileid in webtext.fileids():
    print fileid,'--',webtext.raw(fileid)[:65], '..'

chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print chatroom[123]

    
