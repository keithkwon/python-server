# GET

from urllib.request import urlopen
f = urlopen("http://www.example.com")
print(f.read(3000).decode('utf-8'))


#유니코드 타입 바이트스트링 타이프