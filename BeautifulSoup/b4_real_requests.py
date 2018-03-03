import requests
from bs4 import BeautifulSoup


url = 'https://news.ycombinator.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
response = requests.get(url,headers = headers)
html_doc = response.content 
soup = BeautifulSoup( html_doc, 'html.parser')
# get all content title at hack_news
pids = soup.findAll('a',{'class':'storylink'})
for pid in pids:
    print(pid.string)