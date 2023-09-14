# -*- coding:utf-8 -*-
from test.test_atexit import h2
from jamo.jamo import h2j
from unicode import join_jamos

#pip install jamo(초성/중성/종성 분리)

#영어:a가 한글자
#한글:ㄱ ㅏ ㄱ(초성,중성,종성)이 합쳐져서 한글자

w="똥"
print(w.find("ㄸ"))
a=h2j(w)
print(a)
print(a.find("ㄸ"))


#hangul-utils github 다 필요하지는 않고
#unicode.py만 가져와서
#초성/중성/종성 합치기
w2="ㅎㅡㅇ"
c=join_jamos(w2)
print(c)