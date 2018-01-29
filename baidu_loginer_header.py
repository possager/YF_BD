import requests
from scrapy.selector import Selector
import cookielib


class baidu_header:
    def __init__(self,header):
        self.headers = header

        self.cookiejar = cookielib.MozillaCookieJar()



    def update_cookie(self, cookie_dict):
        self.cookiejar











if __name__ == '__main__':
    headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.baidu.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        }
    baidu_header_class = baidu_header(header=headers)