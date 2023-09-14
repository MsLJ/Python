# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag._okt import Okt
from hanspell.spell_checker import check
from apyori import apriori
#블로그 이름
#그 블로그에서 뭔소리 많이 하나

#정규화,오타교정,동사는 원형
con=MongoClient("195.168.9.65")
db=con.xe
trainData=[]
label=[]
cv=CountVectorizer()
o=Okt()
blognames=[]
for b in db.KakaoBlog.find():
    blognames.append(b["blogname"])
    data=[b["blogname"]]
    title=o.normalize(b["title"])
    title=check(title).checked
    for w, _ in o.pos(title, stem=True):
        data.append(w)
    
    contents=o.normalize(b["contents"])
    contents=check(contents).checked
    for w,_ in o.pos(contents,stem=True):
        data.append(w)
    trainData.append(data)


con.close()
print(trainData)
result=apriori(trainData,min_support=0.1,min_confidence=0.1)
for r in list(result):
    for r2 in r.ordered_statistics:
        l=list(r2.items_base)
        if len(l)==1 and l[0]in blognames:
            print(l[0],"블로그에서")
            print(list(r2.items_add),"라는 말 자주 씀")

            
            
            print(r2.confidence)
            print("----------")
