# -*- coding:utf-8 -*-


# 2차원 list : 객체 list는 어쩌고..
score = [[100, 90, 40], [80, 90, 20]]
print(type(score))  # 무슨 객체인지
print(type(score[0]))
print("----------")
print(score)
print(score[0])
print(score[0][1])
print(score[1][2])
score[1][0]=0
#score[1][0:3]=0 한꺼번에 여러개 값 바꾸는게 불가능 출력은 가능
print(score)
# NumPy(NumPy의:array): 기본 Python list보다 기능 좋은 list
#cmd
#   pip install numpy
import numpy as np # import 모듈명 as 별칭 ->별칭.??
#score2=np.array(score)
score2=np.array(score,dtype=np.float64)#자료형을 지정해서 바꾸고 싶다면 뒤에 dtype을 추가 Python은 지정안하면 자동으로
print(type(score2))
print(score2)#출력형태가 다르다
print(score2[0])
print(score2[0][1])#Python 리스트 스타일
print(score2[1,2])#Numpy스타일
score2[1,0]=100
#Numpy에서는 값을 바꾸는게 가능 Python에서는 안됐는데
score2[1,0:3]=0#slicing(한꺼번에 여러개 값 바꾸기)
print(score2)
print(score2.dtype)#자료형
print(score2.shape)#몇행몇열
print(score2.size)#총 갯수

#Numpy를 pandas/Matplotlib/Tensorflow등이 활용
























