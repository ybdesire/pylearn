from bs4 import BeautifulSoup

html_doc = """
<html><head><title>This is a title</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title.string)# get string in title tag: This is a title
print(soup.find_all('a'))# find all a tag as list
'''
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="htt
p://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="
link3">Tillie</a>]
'''

print(soup.find(id='link3'))
'''
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
'''
