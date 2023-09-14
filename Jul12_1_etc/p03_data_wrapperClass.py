# -*- coding:utf-8 -*-
#J:
#    wrapperClass : 기본형에 해당하는 (int->Inteager)
#                    객체형이 필요할때(List<Integer>)
#                    형변환(Integer.parseInt("1"))
#    int i=10;
#    List<Integer>

#P:
#    이미 기본형자체가 존재X wrapperClass만 쓰는 중
#    객체형밖에 없
#    형변환은 생성자로

a=10
a=str(a)
print(a)
print("-------------------")
#숫자(x,y,z....):
data=input("")
datalist=data.split(",")
hab=0
#int로 형변환 시키고
#그다음 +=하면 오류가 터지는데 그냥 그거 무시하기위해 try: except:쓰면 무시
#그냥 try: except: 쓰면돼는데 생각을 못했다..
#*try except*
for n in datalist:
    try:
        hab+=int(n)
    except:
        pass
print(hab)
