import requests
from scrapy.selector import Selector
import cookielib




headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }


cookiejar=cookielib.LWPCookieJar()
session1=requests.session()


session1.headers.update(headers)
session1.cookies=cookiejar

response1=session1.get(url='https://twitter.com/')

session1.get(url='')