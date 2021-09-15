from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 잘 쓰지 않는 HEAD 요청에 대한 응답에는 헤더만 있고 바디만 오기 때문에 len(data)는 0이 된다.
conn.request('HEAD', '/')
resp = conn.getresponse()

print(resp.status, resp.reason)
print(resp.msg)
data = resp.read()

print(len(data))

print(data == b'')
