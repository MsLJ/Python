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
    'Keyword': ["오염수", 'AI', "디지털", "과학기술정보통신부 ", "방류", "후쿠시마", "LG", "데이터", "수산물", "반도체"],
    'Value': [1453, 1223, 1000, 813, 615, 585, 547, 523, 499, 450]
}
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Keyword', y='Value', palette='Set3')
plt.xlabel('Keywords')
plt.ylabel('Values')
plt.title('IT TOP 10')
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()
