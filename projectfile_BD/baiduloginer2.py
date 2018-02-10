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
from w3lib.url import safe_url_string
from selenium import webdriver


class baiduloger:
    def __init__(self,platform=None,content=None,password=None,type=None,link_ip=None,
                 link_port=None,url=None,userId=None,account=None,
                 account_id=None,cookie=None,link_id=None,title=None):
        self.name=account
        self.name=account
        self.password=password
        self.content=content
        self.platform=platform
        self.type=type
        self.link_ip=link_ip
        self.link_id=link_id
        self.link_port=link_port
        self.url=url
        self.userId=userId
        self.account_id=account_id
        self.cookie_raw=cookie
        self.title=title



















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

        self.basic_file='F:/project_2018/YF_BD/projectfile_BD/'#cookie/Selenium_cookie/

        # self.proxies={
        # 	"http": "http://127.0.0.1:57415",
        # 	"https": "https://127.0.0.1:57415",
        # }



    def initial(self,new=False):#session会自动的设置cookie
        try:
            self._init_cookie_from_selenium()
        except Exception as e:
            print e
            self._init_cookie_from_cookie_existed()



        self.session.cookies=self.cookie

        self.session.headers=self.headers

    def reply_post(self,data,forum_url):

        postdata=self._get_data_for_replyPost(url=forum_url,data=data)

        post_url = 'https://tieba.baidu.com/f/commit/post/add'

        self._update_self_headers_cookie()

        response=self.session.post(url=post_url,data=postdata)
        print response.text

    def publish_post(self,data,forum_board_url):
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




        response1=self.session.post(url=post_url,data=postdata)
        print response1.text


        # self._update_self_headers_cookie()
        # response1=self.session.get(url=forum_board_url,headers=self.headers)
        # selector1=Selector(text=response1.text)
        # tbs_fid= selector1.xpath('//script[contains(text(),"if (!o.hasOwnProperty(propKey) ||")]').re('\'tbs\'\: \"(.*?)\"[\s|\S]*?PageData.forum = \{[\s|\S]*?\'id\': (.*?)\,')

    def share_post(self,toSharepost_url,toforumname,title='分享一下',content='转发一下'):
        postdata=self._get_data_for_sharePost(toshareurl=toSharepost_url,toforumname=toforumname,content=content,title=title)
        post_url='http://tieba.baidu.com/f/commit/share/commitShareApi'
        headers1 = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Host': 'tieba.baidu.com',
            'Origin': 'http://tieba.baidu.com',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',

        }


        headerreferurl=postdata['referurl']
        headerreferurlsafe=safe_url_string(url=headerreferurl)
        headers1['Referer']=headerreferurlsafe
        del postdata['referurl']
        response1 = self.session.post(url=post_url,data=postdata,headers=headers1)
        print response1.text

    def create_usercookie_from_remotedata(self):
        self._create_UesrCookie_from_remoteData()

    def login(self,username=None,password=None):#登陆有可能找不到对应的标签而失败
        if not username:
            username=self.name
        if not password:
            password=self.password

        driver = webdriver.Chrome()
        driver.get(url='https://www.baidu.com')

        login_botton = driver.find_elements_by_xpath('//div[@id="u1"]/a[@name="tj_login"]')
        print login_botton
        login_botton[0].click()

        time.sleep(3)
        driver.find_element_by_xpath('//p[@class="tang-pass-footerBarULogin"]').click()
        time.sleep(3)

        input_name = driver.find_element_by_xpath('//input[@class="pass-text-input pass-text-input-userName"]')
        input_name.send_keys(username)

        input_pwd = driver.find_element_by_xpath('//input[@id="TANGRAM__PSP_10__password"]')
        input_pwd.send_keys(password)

        driver.find_element_by_xpath('//input[@class="pass-button pass-button-submit"]').click()
        time.sleep(10)
        driver.find_element_by_xpath('//input[@class="pass-button pass-button-submit"]').click()

        time.sleep(2)
        driver.get(url='http://tieba.baidu.com/p/5465046117')


        cookies = driver.get_cookies()
        self.cookie_raw=cookies

        self._create_UesrCookie_from_remoteData()
















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

    def _create_UesrCookie_from_remoteData(self):
        cookielist = []
        cookie_remote = json.loads(self.cookie_raw)
        for one_cookie in cookie_remote:
            cookie1 = get_cookie_from_dict(one_cookie)
            cookielist.append(cookie1)

        for onecookie in cookielist:
            self.cookie.set_cookie(onecookie)




    def _init_cookie_from_cookie_existed(self):
        self.cookie.load(self.basic_file+'cookie/LWPcookie/'+self.name)

    def _get_data_for_replyPost(self,url,data):
        self.session.headers['Host'] = urlsplit(url).netloc#这里边的cookiejar基本没有屁用，完全没有起到访问时带参数的功能

        print self.session.cookies

        self.headers['Cookie']=self.cookie_str



        response=self.session.get(url=url,headers=self.headers)
        selector1=Selector(text=response.text)

        # print selector1.xpath('//script[contains(text(),"var topic_thread")]').re(' data \: \{(.*?)\}')
        result = selector1.xpath('//script[contains(text(),"var topic_thread")]').re(
            '.*kw:(.*?)\,.*ie:(.*?)\,.*?rich_text:(.*?)\,.*?floor_num:(.*?)\,.*?fid:(.*?)\,.*?tid:(.*?)\,')
        tbs = selector1.xpath('//script[contains(text(),"var PageData")]').re('"tbs"[\s|\S]*?\: "(.*?)"\,')




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

    def _get_data_for_sharePost(self,toshareurl,toforumname,content,title):
        headers_share_post = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            # 'X-Requested-With': 'XMLHttpRequest',
            'Host': 'tieba.baidu.com',
            'Origin': 'http://tieba.baidu.com',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        response1 = self.session.get(url=toshareurl)
        selector1 = Selector(text=response1.text)
        # tbs_fid_kw = selector1.xpath('//script[contains(text(),"if (!o.hasOwnProperty(propKey) ||")]').re(
        #     '\'tbs\'\: \"(.*?)\"[\s|\S]*?PageData.forum = \{[\s|\S]*?\'id\': (.*?)\,[\s|\S]*\'name\'\: \"(.*?)\"')
        result = selector1.xpath('//script[contains(text(),"var topic_thread")]').re(
            '.*kw:(.*?)\,.*ie:(.*?)\,.*?rich_text:(.*?)\,.*?floor_num:(.*?)\,.*?fid:(.*?)\,.*?tid:(.*?)\,')
        tbs = selector1.xpath('//script[contains(text(),"var PageData")]').re('"tbs"[\s|\S]*?\: "(.*?)"\,')

        # title= selector1.xpath('//head//title/text()').extract()[0]
        urlshare1 = 'http://tieba.baidu.com/f/commit/share/openShareApi?url='+toshareurl+'?sharefrom=tieba&title=' + title + '&desc=' + title + '&comment=&pic='

        response2=self.session.get(url=urlshare1)

        tbs = str(tbs[0])
        fid = str(result[-2].strip('\\').strip('\''))
        kw = result[0].strip('\\').strip('\'')


        refuer_field='转自：[url]'+toshareurl+'?sharefrom=tieba[/url]'
        summary='mark1[br][img pic_type= width=540 height=499]mark2[/img]'
        refuer_field2='转自：[url]http://tieba.baidu.com/p/5536804932?sharefrom=tieba[/url]'
        post_data={
            'ie': 'utf-8',
            'fid': fid,
            'fname': toforumname,
            'title': title,
            'content': content,
            'summary': '',
            'refer_url': refuer_field,
            'vcode': '',
            'vcode_md5': '',
            'tbs': tbs,
            'new_vcode': '1',
            'tag': '11',
            'referurl':urlshare1
        }

        sharedata1 = {
            'ie': 'utf-8',
            'fid': fid,
            'fname': toforumname,
            'title': '转贴:【图片】王思聪微博上晒快递,网友们的评论是亮点!【八卦吧...',
            'content': '树大招风a ',
            #     'summary':'【图片】王思聪微博上晒快递，网友们的评论是亮点！【八卦吧】_百度贴吧[br][img pic_type= width=540 height=499]http://imgsrc.baidu.com/forum/w%3D580/sign=280703446781800a6ee58906813433d6/3332b7fd5266d016f07b64e39c2bd40737fa3580.jpg[/img]',
            # 'refer_url': '转自：[url]http://tieba.baidu.com/p/5536804932?sharefrom=tieba[/url]',
            'vcode': '',
            'vcode_md5': '',
            'tbs': str(tbs),
            'new_vcode': '1',
            'tag': '11',
            'referurl': urlshare1,
        }


        return sharedata1


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
        kw= kw.decode('unicode_escape').encode('utf-8')
        # kw='彭于晏'
        # kw='bigbang'


        mouse_pwd_t=str(int(time.time()*1000))
        # tbs='423ac6d55f0311cd1517471852'
        # tbs = '118dc6e7ef837e821517535260'

        bsk=self._get_bsk(tbs)

        # post_data={
        #     'ie':'utf-8',
        #     'kw':str(kw),
        #     'rich_text':'1',
        #     'floor_num':'0',
        #     'fid':str(fid),
        #     'tid':'0',
        #     'tbs':str(tbs),
        #     # 'tbs':'3bcf204f2288a7e21517361594',
        #     'content':str(content),
        #     'tilte':str(title),
        #     'mouse_pwd_t':mouse_pwd_t,
        #     '__type__':'thread',
        #     'basilisk':'1',
        #     'prefix':'',
        #     'vcode_md5':'',
        #     'mouse_pwd_isclick':'0',
        #     # 'mouse_pwd':'118,115,119,108,121,121,117,116,73,113,108,112,108,113,108,112,108,113,108,112,108,113,108,112,108,113,108,112,73,114,117,121,114,113,73,113,121,114,112,108,113,112,120,112,'+mouse_pwd_t,
        #     '_BSK':str(bsk['bsk']),
        #     # '_BSK':'JVwWUmcLBmUQOX99TW4EAUhdZzEvSxZDVyIJBjdUKDQ+XXhGEzJkXVUTBjkFWUMfLAg8Wxo1ZTp8UkMHdBMeCTAbQC8ELx9WAwIhdXYHHAYcd0dSN0AjfHNRZE0JaSIcGUA4e0ZZGEtzCG4BT2cLcW9GUVNpE0kaZ08RPQA/H1wDFC4IO2kDB1QqRQpnQXdyaxI2Gl0qMBQaXX0jC35eGyBGOBxXcENnfl5BOCtQUEIzEBM8DigTbRdFaXUqFlcNHisGSjZQanI/AnJVE3t0TEIDaGZVAQgaeAplFE9gAHdyXA1SZwsGUS1YcBFDYFRFW0V/dRdKD15SIQYJcBt2cHlnOQFXJjMOVX0Jd1UdBFlyCAh7KWYMfH4MF1lwCQobbFV0OgInGR9YV3RnahRFBh4LDlQgUykofgVoQQNraF8WAn9tRFlYHCwEfVVNcgJnOB8NECAdBkp3Vwl/UHxCAEZFMmR4H1VRXyEUQ2kXMWJzCnIhZgUIX1kRM2ZGFwpbeRloBEthCWt8G1BBfxEWG3RCA2pQfVoSC1ZnbXoUTAUOYUVRcRd8cjJcPxxWZTcJGkNxMQtOXxplSjNBDHxXNzsQTQIpVFZfaRZcMQclBF1GFzc4N1UBG04/DkgxGTY/IkQdCkA6JRoQHz42FFlfGyxtKVEQJEtrLBsNBiRCQW4zEF0rEmARVR40IDs/RgFeUSNLQSBBBT88QCUbVi0XCQxfOHsJTF4KIWU6UBcxFCoxCAQ3Kh1JRDMQcSZNPhNDAx0gAzUJB1JNJB1DB0xqIzJCPwNfZTceB1wxOzBCCEVrWG4WRHIdcBxbU1ExU1cOd0cWbCBpRAJZBSYxaBVBUQx/Xx4kAiNiYAVhWAB/dUhMB3hlVggdLWsEfVhMcgJnKgwUBmkTVxlnTxNuWH5GHEgUdnVgBQFFSyhLBCsGZGpxAmBeBHlxTEQffydWDxBLHkExB0xyRQ==',
        #
        # }

        post_data1 = {
            'ie': 'utf-8',
            'kw': str(kw),
            'fid': str(fid),
            'tid': '0',
            'vcode_md5': '',
            'floor_num': '0',
            'rich_text': '1',
            'tbs': str(tbs),
            'content': content,
            'basilisk': '1',
            # 'title': '这个意境吧是什么鬼',
            'title':title,
            'prefix': '',


            # 'mouse_pwd': '110,107,111,116,105,105,108,108,105,81,105,116,104,116,105,116,104,116,105,116,104,116,105,116,104,116,105,116,104,81,105,105,96,109,108,81,105,97,106,104,116,105,104,96,104,15173792270880',
            'mouse_pwd_t': str(int(time.time()*1000)),
            'mouse_pwd_isclick': '0',
            '__type__': 'thread',
            #     '_BSK':'JVwSUGcLBF83AFZzQyVHElBHMSUvQFkVSX5FHGVTJzwiVXxNXXpmR1UBbWZTHR9YeAR9Q0pyAmUuERIXCFRXWCQSVnMDIANCRgEqNC9WWVRSIhRDaVM0MTxVI0NALCgbWUQ0OQBCXUU5SS1RECQUKC4bDwY3HVBENVlfOg8rAlhGBCk4KUARG1IiBEcxXCk+fVQ/DEYkIRMBHzIlDUpDB2VGPlkbfFAuLQoOETwdSEQmFEc2DiIUURhLKDI0UBdWTGEXQzdGKT4wXDIOQWU3HgdcMTsGTFgaawR9VUpyAmc4Hw0QIB0GXHRXCX0vGTp8SEtnJ2gHTxVpJAkVdxdqcj0BclURMyxQNn1/e0ZdGUtzCDlVEiNda3wTUEF/E0ZKNhxfNhInKVEmEXU9PQdZFUx8RRxnUzM+MkQ5AF1pNhwbVzI6TAQKEmlzMVUKOU4ifh0OByBsBFZnWREoU25MEiQyCRt4CVdSD29dBncFd2dhBWFeH2s3TFcJfWZUFRpFa1huFkRyHXAcW1NRMVNXDndHFmwgaUQCXAImM21ERwZceVIeIA0lYmAFYVgAfn1MQAR4ZVYIHS1rBH1ATHICZ29LUFR2Bh0ZdkwffQB/VApKASQ7KUBZFVB/RRxlB3ZhZgBlXgJlZhxEEWd3VRQYWWUKLAZcahh2Z0xRT2dQFgl/VQJvVXxaEh5WZ214QwBZXTkOSSsVMj8CRCIGXS5sVFVIfQwKTF4AP01/VxE0XRp+A0NPZ1IVCX9VRy0UKVoSBFZnbXoXRQYJfVIXdBlkNGASak19HAgxVx9/O1YPEEk9WipRUnJNdnxEQy4qS01HKRQcak98Vhg9DiszNVIGF3AZRxd1G3ZrcWcfOAV9bV00Qy07AXpPCwJBKxtLYw9pbUhBSw55cGYJWRMzCCcTEC0CJjw1DFV0Vj8ISyAacGR/AH5cAXF2U0QCZHc3TEwIO0FwAU1nFnRoXBw=',
            #     '_BSK':'JVwRUWcLBnwsGwBtQ2BUXFtFf3UgTVh0cG9LBCAEZGpxAmBeBHlxTEQffyJVDxBLBEclXRI8WWhrUFFDbWZNRSEaRCxBAiIQW1drZ2EFInhpe1MPZXQ2ID1VBwpRAi0JWgZuYEoeHElhYxdgMxwUZzIXCgZldkFILhoafyIkBF8HAmphbgtFGQ1/XxRrBHdpcWMxCVI7LVJAAGp5VxsIRWtJbBZEcF4mMg0ET2dCFwl/VUctFClaEgZVZ216UQdCW2FFQnQXfHIfZRwjEWVmE0cRZ3dWHRteeR1uBVJyT3V8REMtEH1oCWlXXm5DdlRSCxQsOzNWHmhfAREWL1JkfHNZYU0JaTAPAFZxdQccCFNpXC1BG3waJmxcW0N0ARAbaVdDbkN2VBVdJWBlaFEXRBt/VQN2dGNiYwY1DFd+JU9EUWliXEgSCnsZagVJYw9+b0tWRncDARwBVx99En1UCkpWdW9qCVdACm9dBDVaNSQcVSMcUi4hURdfKCVIS0UKPFtzVxI/SyJyGBMCKFRXBzYQXzlNOx9eDggyeypEB1JQOUtJNVAoNSMcJABDZSgYG1QpP0hORgY6TTsYEj9bJioXDg1pVUtIMBhWMRVgGUIDACw5dksUWlthD082QSkiKBw8AFAoMBQaXT82FgFHDCddPVUMfEgiLA0ODSRdRko3WUA8EyMaXAgGNyR4CVdWD29dBnQMdGB9EidcEXNkGxRfLjJID11YaxJ9eiscdGVyXBJRZwsEGnxHA3NDIkUSUEd3Z2sSRQIPfEsENQZkanFWMQNALGhfFAd/bURLSwU6TXMWDGEafXwYFA0mRU1EK1VBPg8oGV1CTmUsen4bVkokEUNlVik0NG1wEhFlZglEEWd1AlhECj1BMFpeJFcUKgwIDSIZDQs+VWgxADgfRg9HJjg+QCgXQ29LBCsEZGpxAmBeBHlxTEQffyNWDxBJeB1uA01oDHNoRhw='
            #     '_BSK':'JVwNUWcLBF83AFZzQzhHElBFIyI0RgFeUSNHUipmMiI4XjdHGmk/XS5dPCMNW09JKkc7USNwRWVyXARSZwsEGXVEBG9UfUccSAZ0dWAFRA4MfUsENgdkanEBaV0DZWYcRxFnd1UdHlllCi0FXGoaISsQAhcsXkoLNxRdOw4hXhlKHGUMNEQBXkgoR0UqUSMNcU1yQxEndl9PE29nVRoaXHgZcxYaYRp9fDA0LwkTCAkyRBFlQwIjfCZFaXU5FFcNHjkVUyAZZCNgEmpPAnl8TVkRPGRGFwoPKEQsUVJyT3V8REMtEH1oCWlXXm5DdlRSCxQsOzNWHmhfAREWL1JkfHNEYk0JaXVIRARpYlQeHVBlCiwHXGoYMywLBE9nRhAJf1dDMBI4O1UZFCQwPwkXW0s/S0AqVjMjfVM8AEAsaBsHUjAyFwFZDCVOc0MXPlwoKVIRAjdUSl9pGkM6DykEHB4INXs2QBtQSiVLRSlaNTU1HDwAUCgwFBpdcTMLTl8ELEYrGBEiUSA3EE0NJFxBBy0cQCsOPg8cBggmNi5MGllcLBUKKFAoJTNRIkNDLDYOGl08OwZMWEU6Sy1bEjxaJiwNQ09nXxUJf1UBb1B7RgVbVml1OxFXDR4rBko2UGpyIQNyVRMvJREGVnF1FB8IU2t/NlpNYhprfBJQQX8TXkNoNn19TW4YA0hdZWVqFEIHC3xWCmdFd3JrEnVYcWx2TwFRLnJWHw9aCA1tBkg1WyNpH1NSJwUREyBNUG1QeUcHWVB8Zm8SUAUMaFBiZxlkJWASak1+Jj4UGV88eFEDGklhfzZaGj9PNH4wNUN0AQobflVkEDZ6QhlKJjUnNkAiUlwGDlJqAHVnfwNmTxsCDCk4f3F3CERBDGlvOlcVPxFnHRYTDChUCx1xWwNxUn5OAkRWdG56dhRRXz8OCXAGcX5iBnJDET53X08TOzYIXk9Fa0FuFkRwTDUrGxw='
            #     '_BSK':'JVwWV2cLBlsqBkcSBD8FUQ0CaTU2UAcbWCIEUzYZJTw+QzVDVTslEBBAcSQBQUxFPkExUBEnFDc/DAQNMR1LWyAbVi1NOBlARgsgOT1RHRtdIQhVIFFqPD5TMRtaJipREVw+IglIRB1lRy1dGTlWazAfDAZpWU1YMRpBJk0gGVMLEyw4NEcURRIgAkgwVycifUA1HUAmKhwZUTwlSF5JGyZEM1YfIktlclwWUGcLBF83AFZzQzlHElBFCDggTBlbX2JSCHUVbgc4XjQARDpkMyETbGdKHRFJHmcIAkp5GAYuDg0GElRGYCwBHGpSe1gDXEdtHBJxOHsSbQtPLlBmFzRTOwAaaQcVB1wwMksbHkd5BmwGRmIWdm9HQTAkV0VZLFoGbFZiRQZIS2c7awdPFUQlSmULF2pyJQJyVRN4cUxCB2hnUxUbRWtJbRZEcAl3ak5NQTcABhFnE0YxAjgfXwRHNzY0QRpaFmRHXWVuKDElWSYKEyorGRBufSpGAQgHeAplFExgCXBuS1BSaRNAGmdPERE0ADoSRkUsZngfVUNMOAIKZ0J0cmsSHjp/BWZRV0NudV4NTAglWzoYXCAJZWRcRFQHFBYZMRdAelN+UwMrQndlbEAWUwksVRcnAXNoNAgzXQJ8dUpGBGRmURoPW3sNaHBcfBorbFxbQzFDUU5pV11tQ3ZWRBgSIHt4S0YVBG1VFnQCdmVgAXxNQHhmR1UCbW9UAQgIeAplFE9pCndyXBZSZwsGZRA5f31NbgUCSF1lZmMXRRscIFYEfxckMSJZPAZAIhscOUVtPQMPBks9GX0OXDZNKT0KCAwrEVBEFgFBNg8rXhlKHGUMNEQBXkgoR0UqUSMNcU1yQxE6d19PEyklEUgGSygcfQ5eNlkrLRtNQSQCBhFlE1IzEilaEhpVZ214chxZDX9FCmdWd3JrECQdRixoXxACf21EHxpYfhhqBU8t',
            #     '_BSK':'JVwIUmcLBF83AFZzQyhHElBFCwIWaVcbHD1VBH8XETk/A2JNH2s3TFcJfWZUFRpFa1puFkRyXjIwHRUKKl8EWSQbVzAMZF8QEUceOTtRHEFbbQRJIVAbcCwSfE1eeGZHV1E8JA1BQxoidz54CGBSIHxSQxN2Ex4LIxRfLARgVERYRX93axBEAAp4Vx92BmpyNAFyVRN7dExCA2hmVQEIB3sKZRQKIk0iclwAV2cLBE0kGUA6TW4CAUhdZzEvSxZDVyIJBjFaFSQjWT4IG2BkBlVoMzYQRFwMaUswUBsNGDp8UkMQdxMeC3RMAW9NbhoCSF1lIyhQEBscOFYEfxcLPytZPANSZnFTRRN1AA1DTgY+W396KnAJd3BOWkMSfnMdcVwTHhE8GlU9AiccM1FaAg16SRVzFW4bGWQdIx9pKBQeVn0QAU5BBmAIHFwMP1UicUhVTXUfFxl9Rx1uUHVWYwsBJCUzCkAECWNUEGcZZD5iEmpPAXl1SkUGbGZID11aaxJ/QAwlXWt8CVVBfxNURDYBfjoSPxdXD0snOy9XWVFRLhJVaVYqPyJVfAlBKCkYBh8uMghLBh4gRjtbCXxIJiwbDxdpXlROKxBBcxUjBhwGAiswLk1ZVFIiFEMhGSo/MlEkBlwnaBkaUCg6AUNeRSZaNlMXPhQpPxMETy1YV18qB0pzDSMVUR4OKjk4RAcbUygJUydUNHwhVSIcXCclERdSL3sXTlgGJUQ9VQwjGmt8CVBBfxNqfgk5EXNDLUcSUEd0bmgVWRVSfEUcZ08ufRJ+ckMROXVfTxF4YCYIGFs9SiwRTGIddB9bU1EgUxQYcUdWOgIqEwBfViEyaxBEAAp4Vx92B2NiYxVnKxFlZgpHEWd1KnhmJWsEfUdNcgJnKgwUBmkTShpnTxNtUX1BAF9WdHt4REYVBG0BRylGI3xzUWJNCWl1TUEDcXUHHAhTaVwtQRst',
            #     '_BSK':'JVwTUmcLBk0wG1ArCCMYEBgGKzM1SF0eHjZHfStUMjknVXAMXC0hIFVOf3tGWhhLcwoRYTIcGmt8EFBBfxEWG3RCA2pQfVoSA1ZnbXpRB0JbYUVHdxd8cGAAZF8faydMVwl9IxZYT0VrRG0WRHBMNSsbTUEyBQYRZwVcLBUBE0MZBiIydkcZQkxhAUkmQDV8Mlw/HFZlIg8UXjgkSF5PBS8EKF0QNFcwcg4AESBfUAcqBVYxBD5aRAUXaTs/SxJDVmEESipGIzR9XD8MUj0tEhsfOTgHWEcMJ1xzWww5Xy4wUg8CKFQIQywGRzATNVpcBQQkIzNKG1VfP0tLIFszMjBCfB9WOzcSG1IxNQVfBhoqWjBYEjJZNS1cTUEyAAYRZztmEy1uWhIdVGdtelEHQlthRVV3F3xwYAliXx9rIUxXCX1lVBwdWXwZbhhcPgplZF4VETBUCAk1RxFlQxsfXllVZ3t4QUQVBG8pcwl5ZHxzUWNNCWkiHBlAOHtGXRtLcwp6Azx1CnUqHBJGdwMBGARQAW1UL08DWVR2ZGhHR1ZYfFcQdAB3Z2UFYV8GeGFPRxZqE0YBCBx4CmUWMz9CLjISAExwHxQLbSJaMQUjAUNKKRF3axVbBwVtMGkSA3J5cXEgH18sExgXeDQjSxgZXmcbaRRWG3ATEzJNQylYT05lMlY8CiNfECkPNzg3QFoBCmNXCHYHfmJ/AWFWExolGxRBNHhRHh1Heh59GFwkCmVkXlBWdAYQHnREAGxNbgIBSF1nMS9LFkNXIgkGMVoVJCNZPggbYGQGVWgzNhBEXAxpSzBQGw0YOnxSQw12Ex4Ld0UCaFF5RwFGRSRmeB9VBgd/VwpnWHdyaxIyDkAgKBQGWAI2KFsaAy4KcxYNYxp9fgoTFiAdBkpxVwl/By0aQw9LZyRrB08XD31fFmkXNmNzCnAJUiU3GFkRMWZGFwgTIQUcelwt',
            #     '_BSK':'JVwRUWcLBnwsGwBtQ2BUXltFf3doFUQADnhWF2kXMmFzCnIJRicnCRxcM3cQQnkdO0ExU1Z5GDx+JQ8CMVhSTmUWXDsEEVZNSEtnMmsHTxcMfVYRdQB3YX0SI14Rc2RMRQtte0ZAG0tzCj1VDTlULi0VPgIJRxRBIlcffQ9/VApKVXVmbRVABg9hRVZ2F3xwN1E8HFZlZhxBEWd3AkxGGiwEfUZPcgJlOAsPADFYS0VlB1IxBSMbGENHPncBSxRDVzsCBiZaIjUMEC1NH2stTFcJfSMWWE9Fa1tsFkRwTDUrG01BMgMGEWc7ZhMtbloSGVVnbXoUTAUOYUVSdxd8cGAFYVgHf31PRABxdRMZCFNrWDBHCh1dNC0fBgZpU0heN1lVMAI5BRwJCyokPwkTRV8gAlVpRiM8NxwnBl0tKwpZQzwlAUNeRSZYOlobIhQzMQ5NDyBfQ18tWVAzDj8TVEYLKjQ7URxYUGEDSSZAKzU/RHwAQSAjFBsfMzYJSAYBIFsrWwwpFCsxHQAXLF5KSSQHHzIEIgNSCxVpJz9XBlhQLAtEJEdqIzJCPwNfKyUPBhFxdRMcCFNrZgp4MnIUZS5PQ1lnFBNpYEcBKwM/UwJYQnYWfxdHBAh7UB8jVyJpN1VjWlIqc0xAAmpjUhQbWn0NbQZbZ3xlclwAUWcLBBp1QQNzQyJEElBHd2drEkUCD3xLBDIGZGpxVjEDQCxoXxkBf21EWVgcLAR9WE9yAmUkFkwgCxMICSRGEWVBKhdcGQJpdTsUVw0efF4UdRlkJWASak1+Jj4UGV88eFEDGklhfzZaGj9PNH4wNUN0AQobflVkEDZ6QhlKJjUnNkAiUlwGDlJqAHVnfwNmTxsCDCk4f3F3CERBDGlvOlcVPxFnHRYTDChUCx1xWwNxUn5OAkRWdG56dhRRXz8OCXAGcX5iBnJDES11X08REwIoYQhFa0tuFkRwTDUrGxw=',
            #     '_BSK':'JVwSUmcLBBp1TQNzQy1FElBHIzY2VhAbHD5VBH8Vd2ljAHxNWnhmR1VHLyIBAQgZewplFik5VnRsXE1BMgIGEWUBQSoEYFRAWUV/dzxEGURbYUVRdBd8ch9lHCMRZWYNRBFndUEaaEx7GitWDXUKdXtNIEZ3Axcdc0IKOQMoT1YPVHA2ORJEAg96UxB8BHVkdAJiSgQNZlFXRmx1Xg9nBjNBM1gffw1pbl5JNCxfQEQyBhMRNWxHAERXfncNaiIBCmRHZzVFKjUGVTIkWj1rSEYEc2RSDQIiAXwSeFJwVC41G0EkIFJPRGxVcDcTIxtVRVFxeWoLRgUGf0kXdAxmAzBWMR1aZnFOQh1uYUYBCBt4CmUWGCVWJCoXDg1lQ0VFIRped0hsDRAxCSQjM1MQF10iA0MYFTtyfRI0XhFzZjMgfxF1SA9EWmsSfwZOYQ93a09QT2ddFgl/VUctFClaEgZWZ214Xx0afQNFCmdCcnJrEiAAQD0JGAZAPDABAUgFPFpzUhEzTTRyHQ0MNlQITTcUXjoSYAVVBgFpIDNLEVhJYRdHN1AoJH1fIApdLDZRAVwtewhIRA49QHNXEj9LIjpSDQwmUFBCKhsfOw4vA10PCTF7NVccUFcjS0gkWCN8OVkjG1w7PVEZXD42EERFBytJLRgTNVYyPB8TTzVUVlgqG1IzAy0EHBkENzg2SRdWTD5FCmdUdHJrEGFfB3loXwYAf21EWVgcLAR9VUpyAmc4Hw0QIB0GSHRXCX8VPgNVRkUxZngfV1FLIwRSLFoocCVfAxtBICoaXRp9LER2RAg9QSlRXjNXIzsjQR5nHQZcd1cJfS8ZOnxIS2c5aAdPF0o/EkNpFydhcwpwXgp7dFFXXWx1Xg0YWXgfbwFPYRRlO09DWWUDFBpyRQZuUGBURFhFf3drEEQACnteEn0CanI8AXJVESslDhxfNCQPckslPxg1U1wt'
            '_BSK': bsk['bsk']
        }
        return post_data1






def test():


    def _init_cookie_from_selenium():
        basic_file='F:/project_2018/YF_BD/projectfile_BD/'
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
    postdata=thisclass._get_data_for_replyPost(url='http://tieba.baidu.com/p/5465046117',data='hello,im here')
    print postdata

    post_url = 'http://tieba.baidu.com/f/commit/post/add'



    # response1=requests.post(url=post_url,headers=headers,data=postdata)
    # print json.dumps(postdata)
    #
    # print response1.text





# if __name__ == '__main__':
#     thisclass=baiduloger(name='somepython')
#     thisclass.initial()
#     # thisclass.reply_post(data='hell,wy deustest is good',forum_url='http://tieba.baidu.com/p/5465046117')
#     # thisclass.reply_post(data='搞笑',forum_url='https://tieba.baidu.com/p/5536804932#')
#
#     # test()
#     # thisclass.publish_post(forum_board_url='https://tieba.baidu.com/f?kw=%E5%85%AB%E5%8D%A6',data={'title':'新人求健身方法','content':'我要拥有像彭于晏一样健康的身体'})#http://tieba.baidu.com/f?ie=utf-8&kw=bigbang&fr=search#sub#￥http://tieba.baidu.com/f?kw=彭于晏
#     thisclass.share_post(toSharepost_url='http://tieba.baidu.com/p/5536804932',toforumname='bigbang')


if __name__ == '__main__':
    data_geted = {
        # 'name':'mio1650392zhi@163.com',
        'password': 'll13629056300',
        'link_ip': '192.168.6.8',
        'link_port': '8118',
        'link_id': 1,
        'platform': 'twitter',
        'content': 'this is content',
        'type': '评论',
        'url': 'https://twitter.com/SrBachchan/status/961864009166209024',
        'userId': 1,
        'account': 'somepython',
        'account_id': 1,
        'cookie': '',
    }
    thisclass = baiduloger(**data_geted)
    # thisclass.login_with_selenium()

    thisclass.login()
    # thisclass.reply_post(content='wish healthy with you!',postUrl='https://twitter.com/SrBachchan/status/961864009166209024')
    # thisclass.publish_post(content='报到一下')
    thisclass.thumb_up(thumbumurl='https://twitter.com/warriors/status/961833343141666817')