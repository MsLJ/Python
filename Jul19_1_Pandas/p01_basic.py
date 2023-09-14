# -*- coding:utf-8 -*-

#Numpy(np.array): 
#        기능 좋은 list
#        의미 알아보기가
#        후속기술들 선수과목
#Pandas:Python Data Analysis Library
#       Ms Excel의 표같은
#        R에도
import pandas as pd
a=pd.Series([125,54,23])
print(a)
print(a[0])
#형태는 OracleDB의 테이블과 유사해보인다.
#마치 sequence를 써서 등록할때마다 번호를 매기는 테이블?과 형태가 비슷
print("------")
b=pd.DataFrame()
b["이름"]=["새우깡","양파링","포카칩"]
b["가격"]=[5000,4000,5000]
print(b)
print("-------")
print(b["이름"])#특정필드 조회
print("-------")
print(b.iloc[1])#1번 데이터 조회
print("-------")
#기본적으로는 번호로 찾게 되어있는
print(b.loc[2])

#찾는 기준을 이름으로
b=b.set_index(b["이름"])
print(b)
print("-------")
print(b.loc["새우깡"])

