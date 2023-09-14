# -*- coding:utf-8 -*-
from konlpy.tag._okt import Okt
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from hanspell.spell_checker import check
from wordcloud.wordcloud import WordCloud
#삼국지 1~10
#맞춤법 교정
#정규화
#동사 원형만 세어서
#시각화
fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)
f=open("C:/lee/sam/shhResult.txt","r",encoding="utf-8")
o=Okt()
wc={}
words=""
for l in f.readlines():
    l=l.split("\t")[0].replace("\"","")
    l=check(l).checked
    l=o.normalize(l)
    for w,p in o.pos(l,stem=True):
        if p=="Verb":
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
            words+=w+" "
f.close()
wc=WordCloud(font_path="C:/Windows/Fonts/malgun.ttf",background_color="white").generate(words)
plt.imshow(wc)
plt.show()

# f2=open("C:/lee/sam/shhResult.csv","a",encoding="utf-8")
# for k,v in wc.items():
#     f2.write("%s,%d\n"%(k,v))
# f2.close()






