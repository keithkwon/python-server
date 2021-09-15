from http.client import HTTPConnection
from urllib.parse import urlencode

host = '127.0.0.1:8000'
params = urlencode({
    'language': 'python',
    'name': '권기현',
    'email': 'shkim@naver.com'
})

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/plain',
}

# HTTPConnection Objects
conn = HTTPConnection(host)
conn.request('POST', '', params, headers)

# HTTPResponse Objects
resp = conn.getresponse()
print(resp.status, resp.reason)

data = resp.read()
print(data.decode('utf-8'))

conn.close()
