import urllib.request


url = 'https://api.github.com/events'
fp = urllib.request.urlopen(url)
mybytes = fp.read()
str = mybytes.decode("utf8") 
with open('http_response.txt', 'w', encoding='utf-8') as fw:
    fw.write(str)
fp.close()


