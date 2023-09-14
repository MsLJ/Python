# -*- coding:utf-8 -*-
from random import randint

# 1.가위
# 2. 바위 
# 3.보
#--------
# 뭐:2
# 컴:가위
# 나:바위
# 승
#-------------질때까지 반복...
# 3연승
handTable = [None, "가위", "바위", "보"]
judege = True
win, you, pc = 0, 0, 0
# 수업에서 구현
# 함수 기존 자바에서는 handtable을 위에다 두고 써야하지만 Python에서는 그냥 아래에 두고 써도 문제가없다.(Interpreter방식이기때문)
#그렇기에 비교적 코드가 지저분할수있고 알아보기 힘들것
def printRule():
  for i,h in enumerate(handTable):
   if i!=0:
        print("%d)%s"%(i,h))
    
#Java스러운 재귀함수쪽으로 추진   
def userFire():
    you = int(input("뭐 낼래 1,2,3:"))
    if 1<=you<=3:
        return you
    return userFire()
def comFire():
    return randint(1, 3)
def youandpcPrint():#굳이 이 안에 you와,pc를 넣지않아도 이미 이 함수를 부르기전에 있으면 알아서 자동으로 들어가기에 넣지않아도됀다.
    print("너:", handTable[you])
    print("컴:", handTable[pc])
    print("------------------------")
    





# def youandpcPrint():
#     print("1.가위,2.바위,3.보")
#     global you
#     you = int(input("뭐 낼래 1,2,3:"))
#     global pc
#     pc = randint(1, 3)
#     print("너:", handTable[you])
#     print("컴:", handTable[pc])
#     print("------------------------")
    
def judge():
    if(result == 1 or result == -2):
        print("패배")
        return 3453234
    elif result == -1 or result == 2:
       
        print("승")
        print("------------------------")
        return 1
    else:
        print("무")
        print("------------------------") 
        return 0
    

# 내가 직접 구현
while True:
    printRule()
    you,pc=userFire(),comFire()
    result = pc - you
    youandpcPrint()
    result=judge()
    if result==3453234:
        break
    
    win+=result
    
    
    
    
    
    
    
    
    
    
    
    
    
