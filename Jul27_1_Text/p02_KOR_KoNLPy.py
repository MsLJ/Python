# -*- coding:utf-8 -*-
from konlpy.tag._okt import Okt

#NLTK:한글은 약하고
#KoNLPy:
#    Java로 만들어져 있어서 ->컴에 Java가 있어야
#    Java를 활용하는 Python프로그램 돌리려면:jpype
#        pip install Jpype1
#    pip install konlpy
t="그 무렵 ~국구 동!승@은 유비가? 떠!난 뒤로 밤낮# 없이 왕%자복의 무리와^ 조조 죽일& 일을 의논*했으나 마땅한 계책이 나오지 않$았다."
t+="집에가고싶다 이런... 차는 테슬라 사고싶다.."

o=Okt() #Open Korean Text분석기
        #((구] 트위터 한글 형태소 분석기)
tt="앜ㅋ앜ㅋ앜ㅋ"
a=o.normalize(tt)#정규화(정리)
print(a)
print("---------")

b=o.phrases(t)#어구 추출(의미있는 단위로 나누기)
print(b)
print("---------")
c=o.morphs(t)#형태소 분석
print(c)
print("---------")

d=o.morphs(t,stem=True)#형태소 분석(기본형)
print(d)
print("---------")
e=o.pos(t)#형태소 분석(품사 태그)->
print(e)  #(단어,품사)의 tuple list

for w,p in e:
    print(w,p)
print("------")

f=o.pos(t,join=True)#형태소 분석(품사 태그)->
print(f)            #(단어,품사)의 str list
print("------")

for wp in f:
    print(wp)
print("------")
g=o.pos(t,stem=True)
for w,p in g:
    print(w,p)
print("------")

h=o.nouns(t)#명사만 list로
for w in h:
    print(w)





