import requests
# refered from 
# https://blog.csdn.net/t8116189520/article/details/90904452
# https://gist.github.com/kylehounslow/767fb72fde2ebdd010a0bf4242371594


addr = 'http://localhost:5000'
url = addr + '/api/img'



file_path='001.png'
file_name=file_path.split('/')[-1]
file=open(file_path,'rb')

files = {'file':(file_name,file,'image/jpg')}
r = requests.post(url,files = files)

print(r.text)