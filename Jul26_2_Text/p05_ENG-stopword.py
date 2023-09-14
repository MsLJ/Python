# -*- coding:utf-8 -*-
#pip install nltk
#NLTK(Natural Language ToolKit):한글은 부실
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
#불용어(stopword):별 의미 없는것들
#a,the
s="With baleful weeds and precious-juiced flowers."
s+="The earth that’s nature’s mother, is her tomb;"
s+="Nor aught so good but, strain’d from that fair use,"
s+="Two such opposed kings encamp them still"
s+="Full soon the canker death eats up that plant."
s+="What early tongue so sweet saluteth me?"
s+="Young son, it argues a distemper’d head"
s+="So soon to bid good morrow to thy bed."

#불용어들 다운받기 (처음 한번만)
# import nltk
# nltk.download("stopwords")
#불용어들 list로
sw=stopwords.words("english")
print(sw)
#불용어들 제외하고 단어수 새기
wordCount={}
for word in word_tokenize(s):
    word=word.lower()
    
    if word not in sw:
        if word in wordCount:
            wordCount[word]+=1
        else:
            wordCount[word]=1
for k,v in wordCount.items():
    print(k,v)







