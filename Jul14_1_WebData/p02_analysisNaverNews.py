# -*- coding:utf-8 -*-


f = open("C:/lee/NaverNews.txt", "r", encoding="utf-8")
wcDict={}#str->int 글자로 찾아서 그 글자가 몇번나왔나 찾기위한 키:벨류
         #dict
for line in f.readlines():
    line=line.replace("\n","").replace("\t","").replace(",","")
    #.split("\t")를 쓰면 line[0]에는 제목 line[1]에는 내용만
    #print(line)
    word=line.split(" ")
    for wd in word:
        #for문에 in은 라인[1]에 있는 거를 word로 받아오는 in
        # if문에 in은 wcDict에 포함하는지? boolean형 in
        if wd in wcDict:
            #그 단어가 이 dict에 있으면 +1해주고
            wcDict[wd]+=1
        else:
            #그 단어가 이dict에 없으면 숫자1
            wcDict[wd]=1
for k,v in wcDict.items():
    #dict에 있는 키값과 벨류값을 불러오는건 items()
    print(k,v)





