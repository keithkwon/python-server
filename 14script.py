# cgihttprequest handler는 simple을 상속받고 do_POST가 구현되어 있다.
# 다만 POST중에서 CGI처리기능만 구현되어 있다.

# 웹서버 실험용 CGI 스크립트

import cgi

form = cgi.FieldStorage()


name = form.getvalue('name')
email = form.getvalue('email')
url = form.getvalue('url')

print("Content-Type: text/palin")
print()

print("name is", name)
print("email", email)
print("url", url)
