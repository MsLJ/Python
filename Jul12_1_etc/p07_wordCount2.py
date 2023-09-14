# -*- coding:utf-8 -*-

class WordCount:
    def __init__(self,w,c):
        self.word=w
        self.count=c
    
    def show(self):
        print(self.word,self.count)


#################################

f=open("C:/lee/wcResult.txt","r",encoding="utf-8")
wcs=[]
for line in f.readlines():
    line=line.replace("\n","").split("\t")
    #아까전에 만든 wcline[0]은 키값 line[1]은 카운트값
    wc=WordCount(line[0],int(line[1]))
    wcs.append(wc)
    #그리고 그 dict를 리스트로 다시 담는 왜냐하면 정렬하기위해서
    print(wc.show())
    
#(lambda p1,p2,....:리턴)(값,값...)
#python이 알아서 객체
wcs.sort(key=(lambda wcwc:wcwc.count), reverse=False)

for v in wcs:
    v.show()


f.close()





