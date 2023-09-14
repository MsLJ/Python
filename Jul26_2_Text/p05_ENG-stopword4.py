# -*- coding:utf-8 -*-
import pandas as pd
import nltk
from nltk.corpus import stopwords


df = pd.read_csv("C:/Users/soldesk/Desktop/tt/tcResult.txt", sep="\t", names=["word", "count"])

stop_words = set(stopwords.words('english'))
def remove_stopwords(text):
    tokens = text.split()
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(filtered_tokens)

df['word'] = df['word'].apply(remove_stopwords)

df = df.sort_values(by="count", ascending=False)

print("-----------------")

print(df.iloc[130:150])