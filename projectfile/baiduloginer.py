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

            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 OPR/50.0.2762.67',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
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

        postdata=self.get_data_for_replyPost(url=forum_url,data=data)

        post_url = 'https://tieba.baidu.com/f/commit/post/add'

        self._update_self_headers_cookie()

        response=self.session.post(url=post_url,data=postdata,headers=self.headers)
        print response.text

    def publish_forum(self,data,forum_board_url):
        if not 'title' in data.keys() and 'content' in data.keys:
            print '数据格式不对'
            return

        post_url="http://tieba.baidu.com/f/commit/thread/add"

        self.session.get(url=forum_board_url,headers=self.headers)

        postdata=self._get_data_for_publishPost(url=forum_board_url,data=data)


        self._update_self_headers_cookie()
        self.headers['X-Requested-With']='XMLHttpRequest'
        self.headers['Referer']=forum_board_url.split('#')[0]
        self.headers['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
        self.headers['Host']='tieba.baidu.com'
        self.headers['Accept']='application/json, text/javascript, */*; q=0.01'
        self.headers['Accept-Encoding']='gzip, deflate'
        self.headers['Origin']='http://tieba.baidu.com'
        self.headers['Connection']='keep-alive'

        postdatajson=json.dumps(postdata)
        self.headers['Content-Length']=str(len(postdatajson))
        # self.headers['Cookie']='BAIDUID=CAB1CBD8A60D86E4A369AA261D5ADB1E:FG=1; BIDUPSID=CAB1CBD8A60D86E4A369AA261D5ADB1E; PSTM=1517378938; FP_UID=89d7ca456e59aec79b19350d7f6e9cb6; BDUSS=GszTlIzdnpCV3lHRWRmckVxdUF5alpySDh0Q0pFWFNZZk1QVnVTeTY0dU42cGhhQVFBQUFBJCQAAAAAAAAAAAEAAACPIk~Oc29tZXB5dGhvbgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI1dcVqNXXFac; TIEBA_USERTYPE=7a4a7b316aa9c64d5ea6204e; STOKEN=79e9af52fd5af1b742a0bd346f62257bd6f79fb0076517ee0545a396df5cdc13; TIEBAUID=512142464335555c730a7106; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1517379101; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1517379158; bottleBubble=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1439_21103_17001_20697_20927; 3461292687_FRSVideoUploadTip=1'
        # self.headers['Accept-Language']='zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
        self.headers['Accept-Language']='zh-CN,zh;q=0.9'
        print self.headers
        print postdata

        proxies = {
        	"http": "http://127.0.0.1:8888",
        	"https": "http://127.0.0.1:8888",
        }


        response1=self.session.post(url=post_url,data=postdata,headers=self.headers)
        print response1.text


        # self._update_self_headers_cookie()
        # response1=self.session.get(url=forum_board_url,headers=self.headers)
        # selector1=Selector(text=response1.text)
        # tbs_fid= selector1.xpath('//script[contains(text(),"if (!o.hasOwnProperty(propKey) ||")]').re('\'tbs\'\: \"(.*?)\"[\s|\S]*?PageData.forum = \{[\s|\S]*?\'id\': (.*?)\,')






    def _update_self_headers_cookie(self):
            cookiestr = ''
            for one_cookie in self.session.cookies:
                _cookiestr = one_cookie.name + '=' + one_cookie.value + ';'
                cookiestr += _cookiestr
            self.headers['Cookie'] = str(cookiestr)

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
        self.session.headers['Host'] = urlsplit(url).netloc#这里边的cookiejar基本没有屁用，完全没有起到访问时带参数的功能

        print self.session.cookies

        self.headers['Cookie']=self.cookie_str



        response=self.session.get(url=url,headers=self.headers)
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
        # tbs='5c9333332b2af1061517451051'
        data = {'tbs': tbs}
        datajson = json.dumps(data)
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.connect(('127.0.0.1', 23456))
        sendmsg(datajson, sock=socket1)
        datajson = recvmsg(sock=socket1)
        data=json.loads(datajson)
        socket1.close()
        return data

    def _get_data_for_publishPost(self,url,data):
        self._update_self_headers_cookie()
        headers1 = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'tieba.baidu.com',
            'Referer': 'http://tieba.baidu.com/p/5465046117',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self._update_self_headers_cookie()
        headers1['Cookie'] = self.headers['Cookie']

        print '\n\n'
        print '----------------------------'
        print headers1
        print '================================'
        response1 = self.session.get(url=url)
        # print response1.headers
        # self._update_self_headers_cookie()
        selector1 = Selector(text=response1.text)
        tbs_fid_kw = selector1.xpath('//script[contains(text(),"if (!o.hasOwnProperty(propKey) ||")]').re(
            '\'tbs\'\: \"(.*?)\"[\s|\S]*?PageData.forum = \{[\s|\S]*?\'id\': (.*?)\,[\s|\S]*\'name\'\: \"(.*?)\"')

        content=data['content']
        title=data['title']
        tbs=tbs_fid_kw[0]
        fid=tbs_fid_kw[1]
        kw=tbs_fid_kw[2]
        # kw= str(kw.decode('unicode_escape').encode('utf-8'))
        kw= kw.decode('unicode_escape')
        # kw='彭于晏'
        # kw='bigbang'


        mouse_pwd_t=str(int(time.time()*1000))
        # tbs='423ac6d55f0311cd1517471852'

        bsk=self._get_bsk(tbs)

        post_data={
            'ie':'utf-8',
            'kw':str(kw),
            'rich_text':'1',
            'floor_num':'0',
            'fid':str(fid),
            'tid':'0',
            'tbs':str(tbs),
            # 'tbs':'3bcf204f2288a7e21517361594',
            'content':str(content),
            'tilte':str(title),
            'mouse_pwd_t':mouse_pwd_t,
            '__type__':'thread',
            'basilisk':'1',
            'prefix':'',
            'vcode_md5':'',
            'mouse_pwd_isclick':'0',
            # 'mouse_pwd':'118,115,119,108,121,121,117,116,73,113,108,112,108,113,108,112,108,113,108,112,108,113,108,112,108,113,108,112,73,114,117,121,114,113,73,113,121,114,112,108,113,112,120,112,'+mouse_pwd_t,
            '_BSK':str(bsk['bsk']),
            # '_BSK':'JVwWUmcLBmUQOX99TW4EAUhdZzEvSxZDVyIJBjdUKDQ+XXhGEzJkXVUTBjkFWUMfLAg8Wxo1ZTp8UkMHdBMeCTAbQC8ELx9WAwIhdXYHHAYcd0dSN0AjfHNRZE0JaSIcGUA4e0ZZGEtzCG4BT2cLcW9GUVNpE0kaZ08RPQA/H1wDFC4IO2kDB1QqRQpnQXdyaxI2Gl0qMBQaXX0jC35eGyBGOBxXcENnfl5BOCtQUEIzEBM8DigTbRdFaXUqFlcNHisGSjZQanI/AnJVE3t0TEIDaGZVAQgaeAplFE9gAHdyXA1SZwsGUS1YcBFDYFRFW0V/dRdKD15SIQYJcBt2cHlnOQFXJjMOVX0Jd1UdBFlyCAh7KWYMfH4MF1lwCQobbFV0OgInGR9YV3RnahRFBh4LDlQgUykofgVoQQNraF8WAn9tRFlYHCwEfVVNcgJnOB8NECAdBkp3Vwl/UHxCAEZFMmR4H1VRXyEUQ2kXMWJzCnIhZgUIX1kRM2ZGFwpbeRloBEthCWt8G1BBfxEWG3RCA2pQfVoSC1ZnbXoUTAUOYUVRcRd8cjJcPxxWZTcJGkNxMQtOXxplSjNBDHxXNzsQTQIpVFZfaRZcMQclBF1GFzc4N1UBG04/DkgxGTY/IkQdCkA6JRoQHz42FFlfGyxtKVEQJEtrLBsNBiRCQW4zEF0rEmARVR40IDs/RgFeUSNLQSBBBT88QCUbVi0XCQxfOHsJTF4KIWU6UBcxFCoxCAQ3Kh1JRDMQcSZNPhNDAx0gAzUJB1JNJB1DB0xqIzJCPwNfZTceB1wxOzBCCEVrWG4WRHIdcBxbU1ExU1cOd0cWbCBpRAJZBSYxaBVBUQx/Xx4kAiNiYAVhWAB/dUhMB3hlVggdLWsEfVhMcgJnKgwUBmkTVxlnTxNuWH5GHEgUdnVgBQFFSyhLBCsGZGpxAmBeBHlxTEQffydWDxBLHkExB0xyRQ==',

        }
        return post_data






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

    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        # 'Host': 'www.baidu.com',
        # 'Connection': 'close',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 OPR/50.0.2762.67',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    headers['Cookie']=cookie_str


    # headers1={'Cookie': u'H_PS_PSSID=25641_1451_19036_21091_18560_20697_22157;BAIDUID=FFF65463E0C0FB29F35C72E7F589811D:FG=1;TIEBAUID=512142464335555c730a7106;TIEBA_USERTYPE=cb23caae86d16457394a57d2;PSTM=1517208188;BIDUPSID=FFF65463E0C0FB29F35C72E7F589811D;FP_UID=ed6b032177b72b8bab6894eaa1c7de01;BDUSS=JFS2ktcDRUbGoxOWFzUn5yVlFPbkpJMzFPTlV6dHA0Vm85M2p0RVYtMk9UNVphQVFBQUFBJCQAAAAAAAAAAAEAAACPIk~Oc29tZXB5dGhvbgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI7CblqOwm5ac1;STOKEN=85b237c06a453dce1c5263538ffc00f2cae81a87c8b100bb4eaac1dc5f94d9cd;Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1517208215;wise_device=0;bdshare_firstime=1517210928905;Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1517210966;', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 OPR/50.0.2762.67'}

    thisclass=baiduloger(name='somepython')
    thisclass.initial()
    postdata=thisclass.get_data_for_replyPost(url='http://tieba.baidu.com/p/5465046117',data='hello,im here')
    print postdata

    post_url = 'http://tieba.baidu.com/f/commit/post/add'



    # response1=requests.post(url=post_url,headers=headers,data=postdata)
    # print json.dumps(postdata)
    #
    # print response1.text





if __name__ == '__main__':
    thisclass=baiduloger(name='somepython')
    thisclass.initial()
    # thisclass.reply_forum(data='hell,wy deustest is good',forum_url='http://tieba.baidu.com/p/5465046117')

    # test()
    thisclass.publish_forum(forum_board_url='http://tieba.baidu.com/f?kw=bigbang',data={'title':'新人求健身方法','content':'我要健康的身体'})#http://tieba.baidu.com/f?ie=utf-8&kw=bigbang&fr=search#sub#￥http://tieba.baidu.com/f?kw=彭于晏