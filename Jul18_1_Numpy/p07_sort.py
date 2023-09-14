# -*- coding:utf-8 -*-
import numpy as np

#1차원
a=np.random.randint(1,101,[10])
print(a)
print(a[1:8:2])
print(a[:8:2])#0~(8-1)안쓰면 알아서 끝까지 
print(a[2::2])#2~끝까지 
print(a[::2])#0~끝까지 
print(a[::-1])#역순
b=np.sort(a)# 오름차순
print(b)
c=np.sort(a)[::-1]#넘파이에서는 reverse없으니까 그냥 오름차순시키고 역순으로 진행시키면될것
#2차원
d=np.random.randint(1,101,[3,5])
print(d)
e=np.sort(d)#행 방향 정렬
print(e)
# f=np.sort(d,axis=1)
# print(f)
g=np.sort(d,axis=0)
print(g)
print("-------------------")
print(d)
h=np.sort(d,axis=0)[::-1]#열 방향 역순
                         #얻어 걸림
print(h)
print("-------------------")
print(d)
#내가 생각한 2차원 배열 sort np.sort(d)[::-1]이라고 하면 2차원 배열이 [[]]이렇게 있는데 바깥쪽이 -1이 적용돼고 또 그 안에있는배열이 sort가 걸린다고 생각
#그래서 (d[::-1])로 해봤지만 결과는 똑같고 애초에 그 논리가 아님
# i=np.sort(d[::-1])
i=np.sort(d)[::-1]#행 방향 역순
print(i)
j=[]
print(d)
#2차원 배열에서는 기존에 우리가 하던 방식으로는 안돼고 결과가 안나오기에
#2차원을 그냥 for문 돌려서 1차원 배열로 하나씩 받아서 그걸 그냥 append하면 될것
for row in d:
    j.append(np.sort(row)[::-1])
     
j=np.array(j)
print(j)




