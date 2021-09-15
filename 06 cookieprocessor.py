from urllib.request import Request, HTTPCookieProcessor, build_opener

url = 'http://127.0.0.1:8000/cookie/'

cookie_handler = HTTPCookieProcessor()
opener = build_opener(cookie_handler)

req = Request(url)
res = opener.open(req)

print('첫 리스폰스', res.read().decode('utf-8'))
print('첫 인포', res.info())

print('쿠키자', cookie_handler.cookiejar)

print("--------------------")
data = "language=python&framework=django"
encData = bytes(data, encoding='utf-8')

req = Request(url, encData)
res = opener.open(req)

print(res.info())
print(res.read().decode('utf-8'))
