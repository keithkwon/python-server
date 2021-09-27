from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World")


# HTTPServer 인스턴스를 만들때는 반드시 핸들러를 지정해줘야 한다.
if __name__ == '__main__':
    server = HTTPServer(('', 8888), MyHandler)
    print("Started Webserver on port 8888...")
    print("^c to quit")
    server.serve_forever()
