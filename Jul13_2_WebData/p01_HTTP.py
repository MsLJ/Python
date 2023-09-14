# -*- coding:utf-8 -*-
from http.client import HTTPSConnection




#https://www.google.com/search?q=%E3%85%81%E3%84%B4%E3%85%87%E3%85%81%E3%85%87%E3%84%B4%E3%85%81%E3%85%87%E3%84%B4%E3%85%81%E3%85%87%E3%84%B4%E3%85%81%E3%85%87%E3%84%B4&oq=%E3%85%81%E3%84%B4%E3%85%87%E3%85%81%E3%85%87%E3%84%B4%E3%85%81%E3%85%87%E3%84%B4%E3%85%81%E3%85%87%E3%84%B4%E3%85%81%E3%85%87%E3%84%B4&aqs=chrome..69i57.282986244j0j15&sourceid=chrome&ie=UTF-8
#https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168066000
#http or https
#연결
# huc=HTTPConnection("주소:포트)
huc=HTTPSConnection("www.kma.go.kr")
#요청
#폴더/파일/파라메터/.
huc.request("GET","/wid/queryDFSRSS.jsp?zone=1168066000")
#응답
res=huc.getresponse()
#응답내용
resBody=res.read()
print(resBody)
#응답내용 한글처리해서
print(resBody.decode())











