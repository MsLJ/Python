# -*- coding:utf-8 -*-
#
# error: 프로그램 언어 문법에 안맞게써서 
#     기계어로 번역이 불가능한 상태 
#     최종산출물이 못나오겠고 개발자 잘못

# warning:지저분한 소스(노란줄)
#         문제없이 최종산출물까지 나오는
#        정리해주는게 좋을것
#         개발자 잘못
 
# exception: 프로그램에는 문제없는
#             실행중에 외부적인 요인에 의해 제대로 안되는
#            개발자 잘못-x
#             누군가는 해결해야->개발자가 좀 대비를...

#P:error VS exception?
#.java-컴파일 형식->.class-압축->.jar-실행->
#    error                exception
#.python-Interpreter방식이라서->error랑 exception이랑 구별이 안됌

#J:예외처리 필수
#    .jar로 소스못보고/수정못하게 그곳에 처리 방법을 넣어놓으면? 호출한쪽에서 그 예외처리가 나와야 해결이 가능할것
#    try-catch-finally(직접처리),throws(처리를 호출한쪽에서)
#P:예외처리 필수 아님
#    .py로 주고받는 어차피 오픈소스코드이기에 굳이 안하고싶으면 안해도...
#    try-except-else-finally
# try:
#     x=int(input("x=?"))
#     y=int(input("y=?"))
#     z=x//y
#     print(z)
#     l=[10,20,30]
#     print(l[y])
# except ZeroDivisionError:
#     print("나누기0?")
# except IndexError:
#     print("리스트없는거?")

try:
    x=int(input("x=?"))
    y=int(input("y=?"))
    z=x//y#/로하면 소숫점까지
    print(z,type(z))
    l=[10,20,30]
    print(l[y])
except Exception as e:
    print(e)#e.printstacktrace(); 뭐가 문제인지 보고싶으면
else:
    print("문제없으면 여기가 실행돼는")
finally:
    print("문제있든없든 앞에 리턴보다 먼저 실행돼는")







#asdasasdasdsa
#error? 문법이 맞지않을때 터지는데
#exception? 실행때 터지는데
#python은 error랑 exception이랑 구별이 안됌













































