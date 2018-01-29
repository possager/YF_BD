#_*_coding:utf-8_*_
import requests
import cookielib
import pickle
from cookie_deal import get_cookie_from_dict
from socket_function import *
from scrapy.selector import Selector
from socket_function import sendmsg
from w3lib.url import urlsplit
import json
import time
import copy



class baiduloger:
    def __init__(self,name):
        self.name=name
        self.cookie=cookielib.LWPCookieJar()
        self.session=requests.session()
        self.cookiefile=''
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            # 'Host': 'www.baidu.com',
            # 'Connection': 'close',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 OPR/50.0.2762.67',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.cookie_str=''

        self.basic_file='F:/project_2018/YF_BD/projectfile/'#cookie/Selenium_cookie/


    def initial(self,new=False):#session会自动的设置cookie
        try:
            self._init_cookie_from_selenium()
        except Exception as e:
            print e
            self._init_cookie_from_cookie_existed()



        self.session.cookies=self.cookie

        self.session.headers=self.headers


    def reply_forum(self,data,forum_url):

        postdata=self._get_data_for_replyPost(url=forum_url,data=data)

        post_url = 'https://tieba.baidu.com/f/commit/post/add'
        # response=self.session.request(method='post',url=post_url,data=postdata,headers=self.headers)

        thisheaders=copy.copy(self.headers)

        cookie_str=''
        for one_cookie in self.cookie:
            cookiestr=one_cookie.name+'='+one_cookie.value+';'
            cookie_str+=cookiestr
        thisheaders['Cookie']=self.cookie_str

        # print thisheaders
        # response=requests.post(url=post_url,data=postdata,headers=thisheaders)
        # response=self.session.request(method='post',url=post_url,data=postdata,headers=thisheaders,cookies=self.cookie)
        print self.session.cookies
        # post_url='http://www.baidu.com'
        self.session.headers['Host']=urlsplit(post_url).netloc


        print self.session.headers
        print thisheaders

        response1=self.session.post(url=post_url,data=postdata,headers=thisheaders)
        print response1.text


        # response=self.session.get(url=post_url,headers=thisheaders)
        # print response.text
        # response=self.session.post(url=post_url,data=postdata,headers=thisheaders)

        # print response.headers
        # print response.cookies
        # for i in self.session.cookies:
        #     print i


        # print '\n\n'
        # print response.text





    def _init_cookie_from_selenium(self):
        with open(self.basic_file+'cookie/Selenium_cookie/'+self.name,'r+') as f:
            cookie_list=pickle.load(f)

        for one_cookie in cookie_list:
            cookie_this_dict=get_cookie_from_dict(one_cookie)
            self.cookie_str+=one_cookie['name']+'='+one_cookie['value']+';'
            self.cookie.set_cookie(cookie_this_dict)
        print self.cookie

    def _init_cookie_from_cookie_existed(self):
        self.cookie.load(self.basic_file+'cookie/LWPcookie/'+self.name)

    def get_data_for_replyPost(self,url,data):
        self.session.headers['Host'] = urlsplit(url).netloc
        response=self.session.get(url=url,timeout=10)
        selector1=Selector(text=response.text)

        # print selector1.xpath('//script[contains(text(),"var topic_thread")]').re(' data \: \{(.*?)\}')
        result = selector1.xpath('//script[contains(text(),"var topic_thread")]').re(
            '.*kw:(.*?)\,.*ie:(.*?)\,.*?rich_text:(.*?)\,.*?floor_num:(.*?)\,.*?fid:(.*?)\,.*?tid:(.*?)\,')
        tbs = selector1.xpath('//script[contains(text(),"var PageData")]').re('"tbs"  \: "(.*?)"\,')


        bsk=self._get_bsk(tbs[0])
        # print bsk
        # print result

        post_data = {
            'ie': 'utf-8',
            'kw': result[0].strip('\\').strip('\''),
            'rich_text': '1',
            'floor_num': '94',
            'fid': result[-2].strip('\\').strip('\''),
            'tid': result[-1].strip('\\').strip('\''),
            'tbs': tbs[0],
            'content': data,
            'mouse_pwd_t': str(int(time.time()*1000)),
            '_type_': 'reply',
            'basilisk': '1',
            'files': [],
            '_BSK': bsk['bsk'],
        }
        return post_data

    def _get_bsk(self,tbs):
        data = {'tbs': tbs}
        datajson = json.dumps(data)
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.connect(('127.0.0.1', 23456))
        sendmsg(datajson, sock=socket1)
        datajson = recvmsg(sock=socket1)
        data=json.loads(datajson)
        socket1.close()
        return data




def test():


    def _init_cookie_from_selenium():
        basic_file='F:/project_2018/YF_BD/projectfile/'
        cookie_str=''
        with open(basic_file+'cookie/Selenium_cookie/'+'somepython','r+') as f:
            cookie_list=pickle.load(f)

        for one_cookie in cookie_list:
            cookie_str+=one_cookie['name']+'='+one_cookie['value']+';'
        return cookie_str


    cookie_str=_init_cookie_from_selenium()

    # headers = {
    #     # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    #     # 'Host': 'www.baidu.com',
    #     # 'Connection': 'close',
    #     # 'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 OPR/50.0.2762.67',
    #     'Accept': '*/*',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    # }
    # headers['Cookie']=cookie_str


    headers1={'Cookie': u'H_PS_PSSID=25641_1451_19036_21091_18560_20697_22157;BAIDUID=FFF65463E0C0FB29F35C72E7F589811D:FG=1;TIEBAUID=512142464335555c730a7106;TIEBA_USERTYPE=cb23caae86d16457394a57d2;PSTM=1517208188;BIDUPSID=FFF65463E0C0FB29F35C72E7F589811D;FP_UID=ed6b032177b72b8bab6894eaa1c7de01;BDUSS=JFS2ktcDRUbGoxOWFzUn5yVlFPbkpJMzFPTlV6dHA0Vm85M2p0RVYtMk9UNVphQVFBQUFBJCQAAAAAAAAAAAEAAACPIk~Oc29tZXB5dGhvbgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI7CblqOwm5ac1;STOKEN=85b237c06a453dce1c5263538ffc00f2cae81a87c8b100bb4eaac1dc5f94d9cd;Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1517208215;wise_device=0;bdshare_firstime=1517210928905;Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1517210966;', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 OPR/50.0.2762.67'}

    # thisclass=baiduloger(name='somepython')
    # postdata=thisclass.get_data_for_replyPost(url='http://tieba.baidu.com/p/5465046117',data='hello,im here')
    # print postdata

    postdata={
        'files': [],
          'tbs': u'04a1bae3614a68591517210966',
          '_type_': 'reply',
          'basilisk': '1',
          'ie': 'utf-8',
          '_BSK': u'JVwVUmcLBk0wG1ArCCMYEB4IFiMoTBtQFmRHXWVuKDElWSYKEyorGRBufSpGAQgbeAplFhglViQqFw4NZUNFRSEaXndIbA0QMQkkIzNTEBddIgNDGBU7cn0SPl4Rc2RPRQJqZ1EcG0VrW2wWRHBMNSsbTUEmAAYRZQFBKgRgVFFYRX93axVBBxJvEBVnD2YkI0U1QxE+cF9PES04F1lnDDpbPlMbfForKwxNBSpSUVhpFl8wEilaVhgGKDIpCQZSUitLUSxbIj8mHCAOQSwqCVlcLTIKSFhFPUcvGBI1ViAqFk0AKV5XTiFZXzACLQJZBQlpMzVGAFpbIxMKKkcvNzhefAFSJCFRHVouIwtfU0UlRzxVCjlXKTwfE08oVEpeJxRBcxEpBEMFCSQ7OEQHG00uFUkpWSQxI0NyQxE8dV9PERA4HkRGBSgHahpOcBAQNxAFDDJCBGURVQJvT3xNED0oEmFuDFV2Tj0LQxJQJBs4RH9aAH5qTkMTdRwseWclZQgzXRU1GAA7HQoMbBFnQzcaXjpOekIeWkl2ZWIXWwYPdEd1JFMnIjgfZVwEZ3dLVx9/PlUPEEk9WipRUnJLdXxEQVJ8AxQHZwUAfVtsEFEGFCB7eEtGFQRtVRZ0AnZlYAF8TV54ZkdXUTwkDUFDGiJ3PngIYFIgfFJDAnYTHgsjFF8sBGBUUV5Ff3c8RBlEW2FFSnQXfHIrWH0sfWtoXwUCf21GCB0rbBptQBwjHXVsW1IiYAMWG3EUAj0AKUUGW1MkYWIQTAYLfFAUdAV/ZmcVYl0WfgBfWRE5ZkYXCCccZBMWUnJPdnxEQy0QfWgJaVdSbkN2VgFTVXV7eFZEFQRtVhZ9BWpyJgJyVREHETE5EXF1ARwIU2kabwVJYA12b1JDD3cTHgsxB0Y6TW4YAkhdZSMoUBAbHD1VBH8XETk/A2JNH2swT1cJfWZRHB1beBlsAkst',
          'mouse_pwd_t': '1516754787259',
          'rich_text': '1',
          'content': 'hello,im here',
          'kw': '\xe9\xab\x98\xe8\x80\x83',
          'fid': '970',
          'tid': '5465046117',
          'floor_num': '14',
              }

    post_url = 'https://tieba.baidu.com/f/commit/post/add'

    response1=requests.post(url=post_url,headers=headers1,data=postdata)
    print response1.text





if __name__ == '__main__':
    # thisclass=baiduloger(name='somepython')
    # thisclass.initial()
    # thisclass.reply_forum(data='hell,myenglist is good',forum_url='http://tieba.baidu.com/p/5465046117')

    test()