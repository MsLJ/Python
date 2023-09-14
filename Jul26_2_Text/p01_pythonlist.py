# -*- coding:utf-8 -*-

a=['a','b','c']
b=['d','a','e','c']

for bb in b:
    #list에 특정값이 있나 in으로 체크 가능
    #dict에 특정키가 있나 in으로 체크 가능
    if bb in a:#for문은 원래 in 쓰고
                #a라는 list에 d가 있나
        print(bb)
#b에 있는거 c에 넣기
c=[]
for bb in b:
    c.append(bb)
print(c)
print("-------")
#b에 있는거 d에 넣기
#파이썬에만 있는 위의 코드를 한줄로 쓰기
d=[bb for bb in b]
print(d)
print("-------")

#b에 있는거 중에 a에 없는것만 e에 넣기
e=[] 
for bb in b:
    if bb not in a:
        e.append(bb)
print(e)
print("-------")

#b에 있는거 중에 a에 없는것만 f에 넣기
f=[bb for bb in b if bb not in a]
print(f)












