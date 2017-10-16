# read from file
import json

datas = json.loads('{}')
with open('dst.json') as json_data:
    datas = json.load(json_data)
datas['size']