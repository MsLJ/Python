# -*- coding:utf-8 -*-
from idlelib.iomenu import encoding


#카톡 내보내기 
#채팅내용 txt로

#Python:
#        하드웨어 쪽 한계 1TB 데이터를 RAM이 어떻게 감당을
#        빅데이터에 부적합한
#        전처리 (1TB짜리 데이터를 서버급 컴 여러대로 병렬처리)
#        ->필요없는 데이터는 제외->50MB
#        ->Hadoop(Linux에서만 돌아가는, Java프로그램)

#영어
#I am a boy
#I am hungry,too.
#I was hurt
#한국어
#나는 소년
#나도 배고파
#나 어제 다침

#신호가3
#신호도2
#선생님5
#선생님도4

# 채팅내용부분만 무슨단어가 제일 많이
f=open("C:/lee/kakaotalk2.txt","r",encoding="utf-8")
txt=None
wc={}
for i,line in enumerate(f.readlines()):
    if i>3:
        line=line.replace("\n","")
        if line.startswith("2023"):
            try:
                txt= line.split(" : ")[1]
            except:
                pass
        else:
            txt=line
        if txt!=None and txt!="":
            for word in txt.split(" "):
                #wc라는 dict를 만들고
                #그 dict안에 키값인word가 없으면
                #그냥 바로 값을=1을줘서 count하는
                #만약에 존재하면 +1
                if word in wc:
                    wc[word]+=1
                else:
                    wc[word]=1

f2=open("C:/lee/wcResult.txt","a",encoding="utf-8")
for k,v in wc.items():
    f2.write("%s\t%d\n"%(k,v))
f2.close()


f.close()
















