# -*- coding:utf-8 -*-
#pip install nltk
#NLTK(Natural Language ToolKit):한글은 부실
from nltk.tokenize import word_tokenize, sent_tokenize


t="그 무렵 ~국구 동!승@은 유비가? 떠!난 뒤로 밤낮# 없이 왕%자복의 무리와^ 조조 죽일& 일을 의논*했으나 마땅한 계책이 나오지 않$았다."

t+="집에가고싶다 이런... 차는 테슬라 사고싶다.."

#특수문자 목록 다운받기(처음 한번만)
# import nltk
# nltk.download("punkt")

#특수문자까지 다 뜯어서 Spilit해주는
wt=word_tokenize(t)
print(wt)

#문장 분리
st=sent_tokenize(t)
print(st)




