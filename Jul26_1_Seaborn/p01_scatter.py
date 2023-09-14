# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect


fontFile="C:/Windows/Fonts/malgun.ttf"
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()
plt.rc("font",family=fontName)

#oracledb wm날씨
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="select*from weather_Data"
df=pd.read_sql(sql,con)
con.close()
print(df)


sns.scatterplot(x="W_TEMP",y="W_HUMDITY",data=df,hue="W_DATE",size="W_HUMDITY",palette="magma")
plt.show()