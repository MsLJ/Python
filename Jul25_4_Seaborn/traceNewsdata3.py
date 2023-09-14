# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime
fontFile = "C:/Windows/Fonts/malgun.ttf"  # 폰트파일경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()  # 폰트이름
plt.rc("font", family=fontName)  # 앞으로 한글쓸꺼면 그래프 그릴떄 저 폰트 사용


data = {
    'Keyword': ["연예인", '연예계', "교육", "연예", "행사", "청소년", "문화가", "브랜드", "피프티", "디지털"],
    'Value': [ 990 , 922 , 884  , 824  , 707 , 701  , 698 , 649  , 632,588 ]
}
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Keyword', y='Value', palette='Pastel2')
plt.xlabel('Keywords')
plt.ylabel('Values')
plt.title('Culture TOP 10')
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()
