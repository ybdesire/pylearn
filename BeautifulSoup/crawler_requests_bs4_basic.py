import requests
from bs4 import BeautifulSoup

headers={
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}
res=requests.get("https://news.sina.com.cn/",headers=headers)
html_doc = res.text
soup = BeautifulSoup(html_doc, 'html.parser')
pids = soup.find_all('a', {'target':'_blank'})
for p in pids:
    if 'news.sina' in str(p):
        print(p['href'])

