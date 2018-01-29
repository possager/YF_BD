#_*_coding:utf-8_*_
import socket
import requests
from scrapy.selector import Selector
import json
from socket_function import *
import pickle



def test():
    url='http://tieba.baidu.com/p/5465046117'
    data='hahaheheheihei'

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host':'tieba.baidu.com',
        'Connection':'keep-alive',
        'Accept-Language':'zh-CN,zh;q=0.9',
    }

    with open('F:/project_2018/YF_BD/cookies/baidu_login','r+') as f:
        cookies=pickle.load(f)

    Cookie_str = ''

    for one_cookie in cookies:
        name = one_cookie['name']
        value = one_cookie['value']
        string1 = name + '=' + value + ';'

        Cookie_str += string1

    print Cookie_str

    headers['Cookie']=Cookie_str


    # response=requests.get(url=url,headers=headers,allow_redirects=False)
    response=requests.get(url='http://tieba.baidu.com/p/5465046117',headers=headers,allow_redirects=False)


    selector1=Selector(text=response.text)
    thisforum_data=selector1.xpath('//script[contains(text(),"var topic_thread")]')
    infor=thisforum_data.re(r' data \: \{(.*?)\}')
    with open('F:/project_2018/YF_BD/cookies/response_one_forum','w+') as f:
        pickle.dump(obj=response,file=f)



    data = {'tbs': '1796da2383a8d7601516771376'}
    datajson = json.dumps(data)
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect(('127.0.0.1', 23456))
    sendmsg(datajson, sock=socket1)
    data = recvmsg(sock=socket1)
    print data



if __name__ == '__main__':
    test()