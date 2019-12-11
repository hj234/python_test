import PIL.Image as image
from wordcloud import WordCloud
import imageio
file = "yes-minister.txt"
# bg_pic = imageio.imread('water1.jpg')
bg_pic = imageio.imread('e.jpg')

#背景图片

with open(file,'rb') as f:
    text = f.read()
text = text.decode('utf-8')
wordcloud = WordCloud(mask=bg_pic , background_color='white').generate(text)
wordcloud.to_file('e_wordcloud.jpg')
image_produce = wordcloud.to_image()
image_produce.show()