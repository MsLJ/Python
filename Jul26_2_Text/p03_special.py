# -*- coding:utf-8 -*-
from sys import maxunicode
from unicodedata import category

#unicode:컴퓨터상에 문자 표현하는 방식
#UnicodeTransfFormat-8bit  UTF-8

print(maxunicode)#전체 unicode문자 수
print(chr(1030))#1030번째 unicode문자
print(category('!'))#뭐
#unicode category로 검색해서...
print("------")
special=[]
for i in range(maxunicode):
#     print(category(chr(i)))
    if category(chr(i)).startswith("P"):
        special.append(chr(i))
# print(special)
# print("--------")

f=open("C:/lee/sam/sam10.txt","r",encoding="utf-8")
wordCount={}
for line in f.readlines():
    line=line.replace("\n","")
#     print(line)
    for word in line.split(" "):
        #for문 돌려서 하나씩 꺼내서 다 replace 특수문자 없애는
        for s in special:
            word=word.replace(s,"")
        if word in wordCount:
            wordCount[word]+=1
        else:
            wordCount[word]=1
for k,v in wordCount.items():
    print(k,v)
            

f.close()

