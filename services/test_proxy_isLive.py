#_*_coding:utf-8_*_
import requests




headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }



proxies={
    'http':'http://192.168.8.42:8118',
    'https':'https://192.168.8.42:8118'
}


response1=requests.get(headers=headers,url='https://www.baidu.com',proxies=proxies)
print response1.text