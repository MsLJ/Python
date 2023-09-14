# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime
fontFile="C:/Windows/Fonts/malgun.ttf"#폰트파일경로
fontName=fm.FontProperties(fname=fontFile,size=10).get_name()#폰트이름
plt.rc("font",family=fontName)#앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용


data = {
    'Keyword': ["미국", '한국', "중국", "일본", "반도체", "경제", "AI","새만금", "오염수", "잼버리"],
    'Value': [1377, 1161, 870, 743, 626, 541, 518, 508, 473, 398]
}
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Keyword', y='Value', palette='coolwarm')
plt.xlabel('Keywords')
plt.ylabel('Values')
plt.title('WORLD TOP 10')
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()
