# -*- coding:utf-8 -*-
from hanspell.spell_checker import check


#py-hanspell:개인개발자가 만들어서 github에 올려놓은거
#    pip으로 설치는 안되고
#    github에 있는거 pip로 설치하려면 컴에 git이 필요
#https://git-scm.com/download/win
#64-bit Git for Windows Setup.

#pip install git+https://github.com/ssut/py-hanspell.git

t="그 무렵 ~국구 동!승@은 유비가? 떠!난 뒤로 밤낮# 없이 왕%자복의 무리와^ 조조 죽일& 일을 의논*했으나 마땅한 계책이 나오지 않$았다."
t+="집에가고싶다 이런... 차는 테슬라 사고싶다.."

a=check(t)
print(a)
print("------")
print(a.checked)#교정된 결과
print("---------")
print(a.errors)#몇 개 교정했나
print("--------")
