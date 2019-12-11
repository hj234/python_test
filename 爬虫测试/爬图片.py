import requests
r = requests.get('https://unsplash.com')
f = open('图片.txt','w',encoding='UTF-8')

print(type(r))

#print(r.text)
#f.write(r.text)