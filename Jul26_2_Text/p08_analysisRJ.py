# -*- coding:utf-8 -*-
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer

# 소설책 불러다가 
f = open("C:/lee/t.txt", "r", encoding="utf-8")

# 불용어제거
wc={}
sw = stopwords.words("english")
wnl = WordNetLemmatizer()  # 표제어 추출기
txt = f.read()  # 한번에 다 읽어서 str
wt = word_tokenize(txt)#단어별로 뜯어서
wt = pos_tag(wt)  # 품사태그
    
    
    
# 동사만 원형으로 해서
for w, p in wt:
    w = w.lower()#소문자로 바꿔서
    if w not in sw:#불용어  list에 없는것만
        if p.startswith("V"):  # 품사 V시작하는거
            w=wnl.lemmatize(w, wordnet.VERB)# 원형으로
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1



f.close()
import pandas as pd
wcList=[]
for k,v in wc.items():
    wcList.append({"단어":k,"횟수":v})
print(wcList)
df=pd.DataFrame(wcList)
print(df)
# pd.DataFrame=>csv(필드명/인덱스 까지)
# df.to_csv("C:/lee/rjWC.csv")

# pd.DataFrame=>csv(필드명/인덱스 빼고)
# df.to_csv("C:/lee/rjWC.csv",index=False,header=False)

#횟수 내림차순 정렬해서 뭔 단어 많이썼나
df=df.sort_values(by="횟수",ascending=False)
print(df)
#단어별 횟수 막대그래프
import seaborn as sns
import matplotlib.pyplot as plt
dftop50=df.head(50)
sns.barplot(data=dftop50,x="단어",y="횟수",palette="summer")
plt.show()



#CSV에 적기
# f=open("C:/lee/tRT.csv","a",encoding="utf-8")
# for k, v in wc.items():
#     wcnt="%s,%d\n"%(k,v)
#     f.write(wcnt)
# f.close()


# for line in f.readlines():
#     line=line.replace("\n","")
#     for word in word_tokenize(line):
#         word=word.lower()
#         if word not in sw:
#             if word in wordCount:
#                 wordCount[word]+=1
#             else:
#                 wordCount[word]=1
# for k,v in wordCount.items():
#     print(k,v)






