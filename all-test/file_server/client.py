import requests
import codecs

url = 'http://127.0.0.1:8008'
path = r'T:\111.png'
print(path)

with open(path,'rb') as img_file:
    r = requests.post(url, files=img_file)
    print('start clients')
