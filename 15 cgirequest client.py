from urllib.request import urlopen
from urllib.parse import urlencode

url = "http://127.0.0.1:8888/14script.py"
data = {
    'name': '권기현',
    'email': 'khik@naver.com',
    'url': 'www.naver.com'
}

encData = urlencode(data)
postData = encData.encode('ascii')
f = urlopen(url, postData)
print(f.read().decode('cp949'))
