from bs4 import BeautifulSoup

html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''
soup = BeautifulSoup(html_doc, 'lxml')
find = soup.find('p')
print("find's return type is ",type(find))
print("find's content is ",find)
print("find's Tag Name is ", find.name)
print("find's Attribute(class) is ", find['class'])
