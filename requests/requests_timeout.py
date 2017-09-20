import requests


requests.get('http://github.com', timeout=0.0001)# seconds, modify to 1 fix the timeout error