import requests

url = 'http://baidu.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
response = requests.get(url,headers = headers)
html_doc = response.content 
print(html_doc)