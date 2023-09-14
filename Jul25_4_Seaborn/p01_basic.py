# -*- coding:utf-8 -*-
#pip install seaborn
import pandas as pd
from cx_Oracle import connect
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용
con=connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
sql="SELECT *FROM weather_Data order by  w_date"

df=pd.read_sql(sql,con)
con.close
print(df)

#알아서
# sns.lineplot(data=df,palette="rainbow")

#필드지정
sns.lineplot(x="W_DATE",y="W_TEMP",data=df,palette="rainbow")
plt.title("날씨")
plt.show()

#Matplotlib:np.array대상,직접 다 설정
#Seaborn:Matplotlib을 쓰기 편하게 해주는 lib
#        pd.DataFrame대상
#        자동으로 그림
#        부족한거 Matplotlib으로
#        테마기능





