# -*- coding:utf-8 -*-

#J:  전세계적으로 많이 쓰이는
#    작업한거 공유하는 문화->Maven
#    클래스명이 중복 될거고
#    package:클래스명 중복될때 구분하게해주는 수단
#            패키지명이 중복되면 방법이 없으니
#            com.회사명.프로그램명.주제
#    import :패키지명 생략하고싶을때 쓰는 옵션사항
###########################################
#P :  전세계적으로 많이 쓰이는
#    작업한거 공유하는 문화(심지어 소스공개)
#    클래스명이 중복 될거고
#    package:클래스명 중복될때 구분하게해주는 수단
#            패키지명이 중복되면 방법이 없지만
#            그래도 자유
#    import : 다른모듈에 있는거 쓰려면 해야하는 필수사항


#import animal.pet#import 패키지명.모듈명
#d=animal.pet.Dog("후추",3)
#d.showInfo()
# 
# import animal.pet as ap#import 패키지명.모듈명 as 별칭
# d=ap.Dog("후추",3)    #별칭.클래스명
# d.showInfo()

from animal.pet import Dog#from 패키지명.모듈명 import 가져올거
from animal.pet import Cat
d=Dog("후추",3)             #클래스명
d.showInfo()

#만약에 위에 import가 있고 아래에도 똑같은 이름의 클레스가있으면
#그냥 가까이있는거 불러오는거 함수명도 포함  
#class Cat:
#    pass
c=Cat()
c.showInfo()


































