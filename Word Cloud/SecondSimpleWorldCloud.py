from os import path
from wordcloud import WordCloud
import jieba
filename = "all.txt"
with open(filename,'rb') as f:
    text = f.read()
text = text.decode('utf-8')
wordcloud = WordCloud().generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')


plt.show()