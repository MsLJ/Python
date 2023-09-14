# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm
FontFile = "C:/Windows/Fonts/malgun.ttf"  # 폰트파일 경로
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()  # 폰트이름 정하기
plt.rc("font", family=fontName)  # 앞으로 그래프 그릴 때 저 폰트 사용

df = pd.read_csv("C:/lee/bus2015Result.txt", sep="\t", names=["요일", "합계"])

# print(df)
#####################
def yoilToInt(s):
    d = {"Sun":0, "Mon":1, "Tue":2, "Wed":3, "Thu":4, "Fri":5, "Sat":6}
    if s in d:
        return d[s]
#####################

df1 = df[df["요일"].str.contains("데이터수")]
df1["요일"] = df1["요일"].apply(lambda y:y.replace("_데이터수", ""))
df1["요일순서"] = df1["요일"].apply(yoilToInt)
df1 = df1.set_index("요일순서")
df1 = df1.sort_index()
# df1 = df1.sort_values(by="요일순서")


df2 = df[df["요일"].str.contains("합")]
df2["요일"] = df2["요일"].apply(lambda y:y.replace("_합", ""))

yoil = df1["요일"]
cnts = df1["합계"]
sums = list(df2["합계"])

print(df1)
print("--------")
print(df2)
avgs = []
for i , v in enumerate(cnts):
    avgs.append(sums[i] / v)
    
plt.bar(yoil, avgs)
plt.show()
