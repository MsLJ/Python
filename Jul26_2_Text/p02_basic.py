# -*- coding:utf-8 -*-

#무슨단어가 몇번나오나

f=open("C:/lee/sam/sam10.txt","r",encoding="utf-8")
wordCount={}
for line in f.readlines():
    line=line.replace("\n","")
    print(line)
    for word in line.split(" "):
        print(word)
        if word in wordCount:
            wordCount[word]+=1
        else:
            wordCount[word]=1
            

f.close()
# for k,v in wordCount.items():
#     print(k,v)
import pandas as pd
wordCountDF=pd.DataFrame(wordCount)
print(wordCount)

