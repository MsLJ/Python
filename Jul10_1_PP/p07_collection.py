# -*- coding:utf-8 -*-

#[],List,Set,Map
#Java에서는 charAt을 활용해야하는데
#Python에서는그냥 String에서 배열처럼 쓰기 가능
s="가나다라 마바사"
print(s[1])
print(s[-1])
print(s[0:5:2])
print("----------")

a=[22,423,22,1,21,222,444,555,666]
print(a,type(a))
print(a[0])
print(a[0:4])#0~(4-1)까지 범위 지정
print(a[0:6:2])#0~(6-1)까지 2칸씩
print(a[-1])#역순
print("----------------")
a.append(999)#뒤에 그냥 추가
a.insert(1, 8)#특정 위치에 추가
a[0]=777#수정
del a[2]#삭제
print(len(a))

#a.sort() 오름차순
a.sort(reverse=True)#내림차순
print(a)
print("------------")
b={1,2,3,4,5,6,45,123,44,55,66,77}
print(b)
print(type(b))

c=[123,321,321,321,321,321,321,1,2,3,4,5,6,7,8]
c=set(c)#set으로 변환시켜서 중복된걸 없애고
c=list(c)#다시 list로 변환
c.sort()
print(c)
print("-----------------------------------")
d={"탄수화물":50,"단백질":30}#Map
print(d)
print(type(d))
print(d["단백질"])
print(list(d.keys()))#키 값들만



print(d.values())
print("지방"in d)#키가 있나
print("단백질"in d)
# Java의 List,Map
#Python의 list,dict

#Python의 list:[1,2,3]:JavaScript의 배열
#Python의 dict:{키:값,키:값}:JS의 객체
#P의 list+dict:JS의 JSON





