# -*- coding:utf-8 -*-
# 패키지 없
from _datetime import datetime
from time import strftime
    # datetime.py      #class datetime
# J
#   Date:2000년대를 생각하지않았던 시절에 만들어서
#    deprecated
#   SimpleDateFormat:Date활용을 서포트(Date<->String)

# P
#   datetime:2000년대를 반영해서 만들어져있음



now = datetime.today()  # static 메소드
print(now)

# J
#    캡슐화->now.getYear():2000년대..

# P
#    접근제어자가 없->캡슐화 없
print(now.year)  # 연도
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print("-------------")
# 특정시간날짜
d = datetime(2000, 1, 1)  # Python에서는 그냥 2000년대가 구현이 돼어있기에 생성자에 쓰면됌
print(d)

#d2=input("아무 날짜:(YYYY/MM/DD):")
# 입력받은거를 datetime객체로 (Java때 SimpleDateFormat)
#d2=datetime.strptime(d2,"%Y/%m/%d")
#print(d2)
#d2=datetime.strftime(d2,"%m/%d")
#print(d2)
# d2=d2.split("/")
# d2=datetime(int(d2[0]),int(d2[1]),int(d2[2]))
# print(d2)

#Java때 SimpleDateFormat 같은거
# str->datetime
#d2=datetime.strptime(datetime객체,"패턴")
#datetime->str
#datetime.strftime(str객체,"패턴")

#패턴확인
help(strftime)
print("--------")
bd=input("생일(YYYY/MM/DD):")
bd=datetime.strptime(bd,"%Y/%m/%d")
#print(bd.year)
bda=datetime.strftime(bd,"%A")
#print(bda)

today=datetime.today()
#today=datetime.strptime(today,"%Y")
print("내 나이",today.year-bd.year,"살",bda,"에 태어남")



















