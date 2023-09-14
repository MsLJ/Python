# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect
from sklearn.preprocessing._data import MinMaxScaler
from sklearn.neighbors._classification import KNeighborsClassifier
import numpy as np
from http.client import HTTPSConnection
from json import loads
from flask.app import Flask
from flask.helpers import make_response
from flask.json import jsonify
from _datetime import datetime

#Spring웹사이트
#게시판에 글 쓸때마다 OracleDB에 날씨,색깔
mms=MinMaxScaler()#정규화해줄객체를 계속 만들어줄필요는 없으니까
knc=KNeighborsClassifier(7)
weahters=None
app=Flask(__name__)
day=-1


def trainAI():
    global weahers
    con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
    sql="select*from zoo_weather_color"
    df=pd.read_sql(sql,con)
#     print(df)
    con.close()
    #뭐가 됐든 숫자로 인코딩
    # 날씨를 숫자로 인코딩
    #pandas에 중복떼고 그냥 해주는거 리스트로 만들어주고
    weathers=list(df["ZWC_DESCRIPTION"].unique())
    df["ZWC_DESCRIPTION"]=df["ZWC_DESCRIPTION"].apply(lambda d: weathers.index(d))
    trainData=df[["ZWC_TEMP","ZWC_HUMIDITY","ZWC_DESCRIPTION"]].to_numpy()
    label=df["ZWC_COLOR"].to_numpy()
    trainData=mms.fit_transform(trainData)
    knc.fit(trainData, label)

def getweather():
    huc=HTTPSConnection("api.openweathermap.org")
    huc.request("GET","/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=meric&lang=kr")
    rb=huc.getresponse().read()
    weatherData=loads(rb)
    temp=weatherData["main"]["temp"]
    humi=weatherData["main"]["humidity"]
    desc=weatherData["weather"][0]["description"]
    # temp=float(input("기온:"))
    # humi=float(input("습도:"))
    # desc=input("날씨:")
    #인코딩,처음 나오는 날씨면 -1로
    try:
        desc=weathers.index(desc)
    except:
        desc=-1
    huc.close()
    #파이썬 특유의 tuple을 이용한 return
    return temp,humi,desc
    
    
@app.route("/color.get")
def Colorget():
    global day
    #새벽시간이면
    #날짜바뀌고 첫 호출
    
    todayDay = datetime.today().day
    if day!=todayDay:
        trainAI()
        print("학습")
        day=todayDay
    temp,humi,desc=getweather()
    predictData=np.array([[temp,humi,desc]])
    predictData=mms.transform(predictData)
    result=knc.predict(predictData)[0]
    return make_response(jsonify({"color":"#"+result})),{"Access-Control-Allow-Origin":"*"}
if __name__=="__main__":
    app.run("0.0.0.0",1234,debug=True)


