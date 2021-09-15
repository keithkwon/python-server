import os
from http.client import HTTPConnection
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser


class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def download_image(url, data):
    if not os.path.exists('download'):
        os.makedirs('download')

    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    for x in sorted(dataSet):
        imageUrl = urljoin(url, x)
        basename = os.path.basename(imageUrl)
        targetFile = os.path.join('download', basename)
        print(imageUrl)
        print(basename)
        print(targetFile)

        print('downloading', imageUrl)
        urlretrieve(imageUrl, targetFile)


def main():
    host = input()
    conn = HTTPConnection(host)
    conn.request("GET", '')
    resp = conn.getresponse()

    charset = resp.msg.get_param('charset')
    data = resp.read().decode(charset)
    conn.close()

    print("downloading")
    url = urlunparse(('http', host, '', '', '', ''))
    download_image(url, data)


if __name__ == '__main__':
    main()
