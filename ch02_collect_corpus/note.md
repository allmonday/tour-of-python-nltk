获得文本语料和词汇资源
====

#### 古腾堡计划


nltk.corpus.gutenberg.fileids() 所有古腾堡的书

#### 网络和聊天语料


聊天室内容，随机抓取

#### 布朗语料库


http://icame.uib.no/brown/bcm-los.html
按照文本分类，如新闻，社论等。 是研究文体之间差异很方便的资源

#### 路透社语料库



#### 就职演说语料库


#### 标注文本语料库


#### 其他语言的语料库


udhr 

#### 载入自己的语料库



1. gutenberg.py, 如何包装文本
2. gutenberg_books.py 统计，平均词长，句长等
3. gutenberg_chat.py 网络聊天室内容
4. brown.py 布朗语料库
5. udhr.py 人权宣言多语种比较
6. diy_corpus 导入自定义语料库

##### nltk中定义的基本语料库函数：

 示例 | 描述
 ------|-------
 fileids() | 语料库中的文件
 fileids([categories]) | 对应列表内的文件
 categories() | 语料的分类
 raw() | 原始内容
 raw(fileids=[f1,f2]) | 指定文件的原始内容
 raw(categories=[c1, c2]) | 指定分类中的内容
 words() | 词汇
 setns() | 句子
 abspath(fileid) | 指定文件在磁盘的位置
 encoding(fileid) | 编码
 open(fileid) | 打开文件流
 root() | 到本地安装的语料库根目录的路径 （？）


### 备注：
diy_corpus.py 的中文输出有乱码
