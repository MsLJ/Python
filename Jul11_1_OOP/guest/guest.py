# -*- coding:utf-8 -*-
class guest:
    def hello(self):
        print("안녕하세요(손님)")
    def write(self):
        name = input("이름:")
        age = int(input("나이:"))
        weight = float(input("몸무게:"))
        height = float(input("키:"))
        return name, age, weight, height


        
