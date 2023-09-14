# -*- coding:utf-8 -*-
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

s="With baleful weeds and precious-juiced flowers."
s+="The earth that’s nature’s mother, is her tomb;"
s+="Nor aught so good but, strain’d from that fair use,"
s+="Two such opposed kings encamp them still"
s+="Full soon the canker death eats up that plant."
s+="What early tongue so sweet saluteth me?"
s+="Young son, it argues a distemper’d head"
s+="So soon to bid good morrow to thy bed."

# 품사 태깅 해줄거 다운(처음 한번만)
# import nltk
#nltk.download("averaged_perceptron_tagger")

wt=word_tokenize(s)
#품사 보여주는
wt2=pos_tag(wt)
for w,p in wt2:
    print(w,p)














