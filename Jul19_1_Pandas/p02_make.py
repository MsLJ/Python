# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
# Python list 
a = pd.DataFrame()  # 빈 DataFrame
a["이름"] = ["홍길동", "김치"]  # 변수명["필드명"]=Python lisst
a["나이"] = [10, 20]
print(a)
print("-----------")

# np.array
b = pd.DataFrame()
b["이름"] = np.array(["홍", "김"])  # 변수명["필드명"]=np.array
b["나이"] = np.array([10, 20])  # 변수명["필드명"]=np.array
print(b)
print("-----------")

# 2차원 list/np.array
# c=[["홍",10],["김",20]]
c = np.array([["홍", 10], ["김", 20]])
c = pd.DataFrame(c, columns=["이름", "나이"])

print(c)
print("--------")
# dict+list
d = {"이름":["홍", "이"],
"나이":[10, 20]}
d=pd.DataFrame(d)
print(d)
print("--------")

#*이걸 많이 쓸것*
#list+dict  Json,MongDB와 같은 구조
e=[{"이름":"홍","나이":10}
   ,{"이름":"이","나이":20}]
e=pd.DataFrame(e)
print(e)
print("------------")







