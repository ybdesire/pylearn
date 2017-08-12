import requests


url = 'https://api.github.com/events'
r = requests.get(url)
str = r.text
with open('http_response.txt', 'w', encoding='utf-8') as fw:
    fw.write(str)


