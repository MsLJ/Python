# -*- coding:utf-8 -*-



a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]
c = []
for i in range(0, len(a)):
    c.append(a[i] + b[i])    
print(c)
e = []
for i in range(0, len(a)):
    e.append(a[i] * b[i])    
print(e)

f = []
for i in range(0, len(a)):
    f.append(a[i] * 2)
print(f) 
print("-----------------")
import numpy as np 
a2 = np.array(a)
b2 = np.array(b)
c2 = a2 + b2
# Numpy리스트는 더하면 각 자리에 더해주는 만약 Python으로 구현하려면 위의 for문 append를 썼어야했다.
# 같은 모양끼리는 자리같은것끼리 계산
print(c2)
d2 = a2 * b2
print(d2)

e2 = a2 * 3 # (1x2)*(1)
            # broadcasting:다른 모양이면 차원수 높은쪽에 맞춰서 항목별로 계산
print(e2)
print("----------")

name=np.array(["hongcha","leesanghannala","kimchi"])
kor=np.array([100,90,80])
eng=np.array([10,60,70])
mat=np.array([30,40,50])
avg=(kor+eng+mat)//3    #//3은 broadcasting적용
print(avg)
over50=avg>50           #boolean형도 가능할것
print(over50)

print(avg[over50])      #masking:위치에 True인것만
print(name[over50])     #평균 50점 넘는 학생이름
print(name[kor>90])

#영어점수가 50~80사이인 학생이름 
#masking때는 and/or대신 &/|를 써야
print(name[(eng>50) & (eng<80)])
#&&는 앞에 조건이 부합하면 조건검사를 거기서 멈추는 &는 앞에 조건이 부합하든말든 그냥 다 조건검사
#||랑|도 같음


