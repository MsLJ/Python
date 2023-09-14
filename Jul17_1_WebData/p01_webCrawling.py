# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

#BD분석용/AI훈련용 데이터 구축
#1) 직접 발로(아침에 학원올때마다 노약자석 체크...)
#2) 완성된 CSV파일 같은거 구하거나
#3) 웹 데이터 활용
#   XML파싱
#   JSON파싱      프로젝트때 내가 그 데이터를 받기위해 어떤형식으로 했고~~를 과시
#   XML/JSON이 없으면?
#    ->웹 크롤링(웹 사이트에서 가져오는) 
#   ->HTML파싱
#    우리가 기존에 해왔던 XML/JSON파싱은 이미 공제된데이터여서 파싱하기 편한데
#    HTML은 애초에 디자인하기위해 하는것이기에 HTML을 파싱하러면 힘들것
#    그리고 법적문제,보안상 사용불가,그렇기에 XML/JSON데이터를  최대한 구하는쪽으로
#########################################################
#HTML파싱
#        Python:BeautifulSoup
#        Java:JSoup.jar

#cmd
#  pip install bs4
######################################################
#https://sdgn-djvemfu.tplinkdns.com/sns.get?page=2
huc=HTTPSConnection("sdgn-djvemfu.tplinkdns.com")
huc.request("GET","/")
resBody=huc.getresponse().read()
#print(resBody.decode())
###################################################
#XML:fromstring()    ->getiterator()/find()
#JSON:loads()        ->list/dict
#HTML:BeautifulSoup()->find()

#                            내용,내장html파서
cafeSNSData=BeautifulSoup(resBody,"html.parser",from_encoding="utf-8")
#???.select(CSS선택자)
snsTxts=cafeSNSData.select(".aSNSTxt2")
for st in snsTxts:
    print(st.text)#???.text
    print("-----")

huc.close()









