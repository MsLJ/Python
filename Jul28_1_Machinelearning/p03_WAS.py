# -*- coding:utf-8 -*-
from flask.app import Flask
from flask import request
from flask.json import jsonify
from flask.helpers import make_response

#pip install flask

#Python WAS:
#        규모있는 django-Spring/SpringBoot/Node.js/...
#        가벼운 flask
#

#BD/AI한 결과를 그냥 콘솔에?
#BD/AI한 결과를 JSON으로 주면:어디서든

app=Flask(__name__)

@app.route("/test")
def test():
    return "hi"
@app.route("/param.test")
def paramTest():
    xxx=int(request.args.get("x"))#request.args.get("파라메터명")
    yyy=int(request.args.get("x"))#request.args.get("파라메터명")
    return str(xxx+yyy)#응답은 또 글자로 해야해서 마지막에str형변환 필요
@app.route("/json.test")
def jsonTest():
    xxx=int(request.args.get("x"))#request.args.get("파라메터명")
    yyy=int(request.args.get("x"))#request.args.get("파라메터명")
    zzz=xxx+yyy
    d={"sum":zzz}
    # loads(...):JSON->Python Collection
    # jsonify(...):Python Collection->JSON
    j=jsonify(d)
    resBody=make_response(j)
    resHeader={"Access-Control-Allow-Origin":"*"}
    
    return resBody,resHeader
if __name__=="__main__":#이 파일 실행했을때(import 말고)
    app.run(
        "0.0.0.0",#접속을 허용해줄 컴 주소
        9898,       #flaskWAS 포트번호
        debug=True  #로그출력
        )







