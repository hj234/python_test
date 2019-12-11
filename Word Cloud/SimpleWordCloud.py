import PIL.Image as image
from wordcloud import WordCloud
filename = "yes-minister.txt"
with open(filename,'rb') as f:
    text = f.read()
text = text.decode('utf-8')
wordcloud = WordCloud().generate(text)
image_produce = wordcloud.to_image()
image_produce.show()