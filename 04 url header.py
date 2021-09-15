from urllib.request import urlopen, Request
from urllib.parse import urlencode

url = 'http://127.0.0.1:8000'
data = {
    'name': '김석훈',
    'email': 'shkim@naver.com',
    'url': 'http://www.naver.com',
}


encData = urlencode(data)

print('이게 데이터임', encData)

postData = bytes(encData, encoding='utf-8')

print('이게 포스트 데이터임', postData)

req = Request(url, data=postData)
print('이게 리퀘스트 인스턴스임', req)

req.add_header('Content-Type', 'application/x-www-form-urlencoded')

print('이게 헤더 추가 리퀘스트 인스턴스임', req)

f = urlopen(req)

print("이게 f", f)

print(f.info())
print(f.read(500).decode('utf-8'))