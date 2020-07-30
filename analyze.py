# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

def returnDataFrameOF(dataset):
    return pd.read_csv(dataset, encoding ="utf-8", index_col=0)

def barPlotOf(dataFrame, xlabel, ylabel, title):
    plt.figure(figsize=(15,10))
    dataFrame.size().sort_values(ascending=False).plot.bar()
    plt.xticks(rotation=50)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def wordCloudOf(dataFrame):
    text = ""
    for i in dataFrame:
        if(type(i) == str):
            text = text + " " + i
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

filename=r"./data/births.csv"
topic="date"
df = returnDataFrameOF(filename)
dates = df.groupby(topic)
barPlotOf(dates, "Month-Date", "Number of Famous People Dead", "Months Vs. Deaths")






