import requests
from lxml import etree

with open("豆瓣音乐top250.txt", "a", encoding="utf-8")  as f:
    for i in range(10):
        url = "https://music.douban.com/top250?start={}".format(i*25)
        headers = { "User_Agent": "Mozilia/5.0(compatible: MSIB 5.5: Windows 10)"}
        data = requests.get(url,headers = headers).text
        s = etree.HTML(data)

        musics = s.xpath('//*[@id="content"]/div/div[1]/div/table')

        for music in musics:
            music_name = music.xpath('./tr/td[2]/div/a/text()')[0].strip()
            music_author = music.xpath('./tr/td[2]/div/p[1]/text()')[0].strip()

            f.write("歌名：{}\n".format(music_name))
            f.write("作者：{}\n".format(music_author))
            f.write("\n")
