# -*- coding:utf-8 -*-
from cx_Oracle import connect



#OracleDB 서버
###################################################
#    SQLPlus:OracleDB서버에 접속해서 제어하는 프로그램(정품)
#            ->cmd기반 불편
#    EclipseIDE로 OracleDB를 제어하자



###################################################
#J
#    DB메이커가 다양한데 그걸 Java에서 어찌 다 감당을
#    각 DB마다 연결할때 쓰는 driver가 필요
#    ojdbc???.jar->maven
###################################################
#P
#    DB메이커가 다양한데 그걸 Python에서 어찌 다 감당을
#    각 DB마다 연결할때 쓰는 driver가 필요
#    cx_Oracle.py(ojdbc???.jar를 사용)->pip(npm)
#    pip install cx_Oracle
###################################################
#    cx_Oracle.py사 ojdbc??.jar가 어디에 있는지 모르기에 찾을수있게
#        instantclinet폴더 경로 복사해놓고
#            C:\lee\instantclient_21_9
#        PATH설정
#            내PC-속성-고급 시스템 설정
#            고급 - 환경 변수 ->위 공간은 지금 로그인한 윈도우 계정에만 아래는 모든 계정 적용
#            Path에 새로만들기 그 안에 경로넣기 (잘못건들면 윈도우 포맷해야함)

#     그냥 아무것도 없는 베이스였다면 상관없지만 기존에 아나콘다를 설치해놔서 겹쳐서 자동완성이 뜨지않아서 추가로 경로설정을 해준..
#     Window-preferences
#     Pydev- Interpreters- Python Interpreter
#     -Forced Builtins-New-cx_Oracle추가
# sqlplus,ojdbc




#cmd
#    pip install 이름 

try:
        #sqlplus에서 연결할때 쓰는 양식
        #sqlplus 아이디/비번@주소:포트/SID

    con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
    print("성공")
except Exception as e:
    print(e)


# create table jul13_coffee(
#    c_name varchar2 (100 char)primary key,
#    c_price number(5) not null
#      
#  );





