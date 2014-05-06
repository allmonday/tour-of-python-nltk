chapter 01: hello nltk
---
samples
===
1. search_text.py
2. plot_dispersion.py,绘制各个单词的文本内分布情况
3. freq_len.py, 找出长度大于15的单词
4. freqCnt.py, 找出出现频率最高的单词，并绘制累增曲线
5. bigrams.py, 统计搭配出现最多的双字词组
6. compare_operator.py, 列表表达式


functions of freq_dispersion..
===
 sample | description
 ------|------
 fdist = FreqDist(samples) | 创建分布,大到小排列
 fdist.inc(sample) | 增加样本
 fdist.freq('monstrous') | 给定样本的频率,占总量的百分比
 fdist.N() | 样本总数
 fdist.tabulate() | 频率分布表
 fdist.plot() | 频率分布图
 fdist.plot(cumulative=True) | 累计频率分布图
 fdist1 < fdist2 | 样本在1中出现的频率是否小于2 (*未测试)

自动理解自然语言
=====
#### 歧义消除
    消除歧义需要使用上下文，利用相邻词汇有相近含义这样一个简单的事实
#### 指代消解
    the thieves stole the paintings, they were subsequently sold/ caught/ found
    不同的词使得they指代的对象也不同

