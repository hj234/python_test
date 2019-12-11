# wordcloud 生成中文词云

import PIL.Image as image
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from imageio import imread

# 读入一个txt文件
with open("all.txt",'rb') as f:
    comment_text = f.read()
comment_text = comment_text.decode('utf-8')
# 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
cut_text = " ".join(jieba.cut(comment_text))
color_mask = imread("water1.jpg")
cloud = WordCloud(
    # 设置字体，不指定的话会乱码
    font_path="STSONG.TTF",
    # 设置背景色
    background_color="white",
    # 词云形状
    mask=color_mask
)
# 产生词云
word_cloud = cloud.generate(cut_text)
# 保存图片
word_cloud.to_file("1.jpg")
image_produce = word_cloud.to_image()
image_produce.show()
