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
import re
from selenium import webdriver



class twitter:
    '''
    所有的cookie数据最终都是pickle之后存储的,取得的cookiepickle对象放在self.cookie_raw中
    在selenium登陆后，dict类型的cookie也经过了处理，变成了LWPcookie对象

    这是之前的打算，现在打算的是：直接存json的cookie

    '''


    def __init__(self,platform=None,content=None,password=None,type=None,link_ip=None,
                 link_port=None,url=None,userId=None,account=None,
                 account_id=None,cookie=None,link_id=None,title=None,guidance_id=None):
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
        self.guidance_id=guidance_id







        self.cookie=cookielib.LWPCookieJar()
        self.session=requests.session()
        self.session.cookies=self.cookie
        self.cookiefile=''
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.cookie_str=''

        self.session.headers.update(self.headers)
        self.proxy_dict={
            'http':'http://'+self.link_ip+':'+self.link_port,
            'https':'https://'+self.link_ip+':'+self.link_port
                        }
        self.session.proxies=self.proxy_dict





        self.basic_file='F:/project_2018/YF_BD/projectfile_twitter/'
        #专门针对这个twitter而设计的
        self.mainpagehtml=''
        self.authenticity_token = ''

        if self.link_ip:
            proxies_dict={
                'http:':'http://'+self.link_ip+':'+self.link_port,
                'https':'https://'+self.link_ip+':'+self.link_port
            }
            self.session.proxies=proxies_dict

    # def login(self,username=None,password=None):
    #     if username:
    #         username=self.name
    #     if password:
    #         password=self.password
    #
    #
    #     postdata=self._get_login_postdata(username=username,password=password)
    #     print postdata
    #     loginresponse=self.session.post(url='https://twitter.com/sessions',data=postdata,headers=self.headers)
    #     selector2=Selector(text=loginresponse.text)
    #     self.mainpagehtml=loginresponse.text#因为主页中有很多需要的值，比如后边点赞需要用到的js。
    #     self.authenticity_token = selector2.xpath('//input[@name="authenticity_token"]/@value').extract()[0]
    #
    #     print loginresponse.status_code

    def login_with_selenium(self,username=None,password=None):
        if not username:
            username=self.name
        if not password:
            password=self.password


        if self.link_ip:
            proxy=self.link_ip+':'+self.link_port
            logindriver=self._add_proxy_to_selenium(proxy=proxy)
        else:
            logindriver = webdriver.Chrome()


        logindriver.get(url='https://twitter.com/login')
        username_div=logindriver.find_element_by_xpath('//div[@id="page-container"]//div[@class="signin-wrapper"]//input[@name="session[username_or_email]"]')#//div[@id="page-container"]//div[@class="signin-wrapper"]//input[@name="session[username_or_email]"]
        password_div=logindriver.find_element_by_xpath('//div[@id="page-container"]//div[@class="signin-wrapper"]//input[@name="session[password]"]')
        username_div.click()
        username_div.send_keys(username)

        password_div.click()
        password_div.send_keys(password)

        loginButton=logindriver.find_element_by_xpath('//button[@class="submit EdgeButton EdgeButton--primary EdgeButtom--medium"]')
        loginButton.click()


        cookies_raw_list=logindriver.get_cookies()
        self.cookie_raw=cookies_raw_list
        cookie_list=[]
        for onecookie in cookies_raw_list:
            cookie1=get_cookie_from_dict(onecookie)
            cookie_list.append(cookie1)
            self.cookie.set_cookie(cookie1)


        self.save_user_Cookie()
        self.save_user_Cookie_local()
        self._update_authenticity_token()



    def publish_post(self,content=None):
        if not content:
            content=self.content


        postdata={
            'authenticity_token':self.authenticity_token,
            'batch_mode':'off',
            'is_permalink_page':'false',
            'place_id':'',
            'status':content,
            'tagged_users':'',
            'weighted_character_count':'true',
        }

        headers1={
            # ':authority':'twitter.com',
            # ':method':'POST',
            # ':path':'/i/tweet/create',
            # ':scheme':'https',
            'accept':'application/json, text/javascript, */*; q=0.01',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'content-length':'168',
            'origin':'https://twitter.com',
            'referer':'https://twitter.com/',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
            'x-requested-with':'XMLHttpRequest',
            'x-twitter-active-user':'yes'
        }


        try:
            response_post = self.session.post(url='https://twitter.com/i/tweet/create', headers=headers1, data=postdata)
            response_json=response_post.json()
        except Exception as e:
            print e
            print '发帖失败'
            return False
        try:
            if response_json['tweet_id'] and response_post.status_code<300:
                print '发帖成功'
                return  True
            else:
                print '发帖失败'
                return False
        except Exception as e:
            print e
            print '发帖失败'
            return False

    def reply_post(self,content=None,postUrl=None):
        if not content:
            content=self.content
        if not postUrl:
            postUrl=self.url


        postdata=self._get_replyPostdata(content=content,postUrl=postUrl)
        posturl='https://twitter.com/i/tweet/create'

        # headers1 = {
        #     # ':authority':'twitter.com',
        #     # ':method':'POST',
        #     # ':path':'/i/tweet/create',
        #     # ':scheme':'https',
        #     'accept': 'application/json, text/javascript, */*; q=0.01',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'zh-CN,zh;q=0.9',
        #     'content-length': '',
        #     'origin': 'https://twitter.com',
        #     'referer': 'https://twitter.com/',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        #     'x-requested-with': 'XMLHttpRequest',
        #     'x-twitter-active-user': 'yes'
        # }


        headers1 = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://twitter.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        }

        replyresponse=self.session.post(url=posturl,data=postdata,headers=headers1)
        print replyresponse.text
        responseJson= replyresponse.json()
        if replyresponse.status_code<300 and replyresponse.json()['tweet_id']:
            print '评论成功'
            return True
        else:
            print '评论失败'
            return False

    def thumb_up(self,thumbumurl=None):
        if not thumbumurl:
            thumbumurl=self.url
        data_post=self._get_thumbupdata(thumbupUrl=thumbumurl)
        postid=thumbumurl.split('/status/')[1]
        authorization=data_post['authorization']
        x_csrf_token=data_post['x_csrf_token']
        post_data=data_post['post_data']
        thumburl=post_data['thumburl']
        postid=post_data['postid']

        postdata_thumbup={
            'id':postid,
            'lang':'zh-cn',
            'tweet_stat_count':'0'
        }

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-length': '42',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://twitter.com',
            'referer': 'https://twitter.com/?logged_out=1&lang=zh-cn',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
            'x-twitter-active-user':'yes',
            'x-twitter-auth-type':'OAuth2Session',
        }
        headers['authorization']=authorization
        headers['x-csrf-token']=x_csrf_token

        response1=self.session.post(url='https://api.twitter.com/1.1/favorites/create.json',headers=headers,data=postdata_thumbup)
        print response1.text

        try:
           response1_json= response1.json()
        except Exception as e:
            print e
            print '点赞失败'
            return False
        if response1_json['id'] and response1.status_code<300:
            print '点赞成功'
            return True
        else:
            print '点赞失败'
            return False

    def share(self,shareposturl=None,content=None):
        if not shareposturl:
            shareposturl=self.url
        if not content:
            content=self.content
        postdata=self._get_share_postdata(shareposturl=shareposturl,content=content)

        headers1 = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-length': '168',
            'origin': 'https://twitter.com',
            'referer': shareposturl,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-twitter-active-user': 'yes'
        }

        shareurl='https://twitter.com/i/tweet/create'
        shareResponse=self.session.post(url=shareurl,data=postdata,headers=headers1)
        print shareResponse.text

    def save_user_Cookie(self):
        # cookielistpickle=self._get_cookie_pickle()
        #因为要求存list类型的，所以这里改了


        # cookie_dict_list=[]
        # for onecookie in pickle.loads(cookielistpickle):
        #     cookie1_name=onecookie.name
        #     cookie1_value=onecookie.value
        #
        #     cookiedict={
        #         'name':cookie1_name,
        #         'value':cookie1_value
        #     }
        #     cookie_dict_list.append(cookiedict)



        cookiejson=json.dumps(self.cookie_raw)
        post_cookie_dict={
            # 'cookie':cookie_dict_list,
            'cookie':cookiejson,
            'account_id':self.account_id,
            'link_id':self.link_id,
            'guidance_id':self.guidance_id,
        }

        cookieupdate_url='http://192.168.6.145:8081/action/cookie_update'

        self.session.post(url=cookieupdate_url,data=post_cookie_dict)

    def create_usercookie_from_remotedata(self):
        self._create_UesrCookie_from_remoteData()
        self._update_authenticity_token()

    def save_user_Cookie_local(self):
        with open(self.basic_file+'cookie/LWPcookie/'+self.name+'2','w') as f:
            cookielist=[]
            for one_cookie in self.cookie:
                cookielist.append(one_cookie)

            pickle.dump(cookielist,f)


    def get_user_cookie_local(self):
        with open(self.basic_file+'cookie/LWPcookie/'+self.name+'2','r') as f:
            cookielist1=pickle.load(f)

            for onecookie in cookielist1:
                self.cookie.set_cookie(onecookie)
            self._update_authenticity_token()








    def _get_share_postdata(self,shareposturl,content):
        # sharepostid=shareposturl.split('/status/')[1]
        attachment_url=shareposturl


        postdata={
            'attachment_url':attachment_url,
            'authenticity_token':self.authenticity_token,
            'status':content,
            'weighted_character_count':'true'
        }
        return postdata

    def _get_thumbupdata(self,thumbupUrl):
        # destroyurl='https://api.twitter.com/1.1/favorites/destroy.json'
        postid=thumbupUrl.split('status/')[1]


        selecotr1 = Selector(text=self.mainpagehtml)
        initjs_url = selecotr1.xpath('/html/head/link[@rel="preload"]/@href').re(
            'https\:\/\/abs\.twimg\.com\/k\/zh-cn\/init\.zh-cn\..*?\.js')[0]
        initjsResponse = self.session.get(initjs_url, headers=self.headers)
        Re_find_K = re.compile('e\.a="(.*?)"')
        value_K = Re_find_K.findall(initjsResponse.text)
        kvalue = value_K[0]

        authorization = 'Bearer ' + str(kvalue)
        x_csrf_token=''
        for onecookie in self.session.cookies:
            if 'ct0' in onecookie.name:
                x_csrf_token= onecookie.value

        data_headers={
            'authorization':authorization,
            'x_csrf_token':x_csrf_token,
            'post_data':{
                'thumburl':thumbupUrl,
                'postid':postid,
            }

        }
        return data_headers

    # def get_exisitedUser_and_authenticity(self):
    #     self._get_user_from_exisitedcookie()
    #     self._update_authenticity_token()

    def _get_login_postdata(self,username,password):
        response1 = self.session.get(url='http://www.twitter.com', headers=self.headers)
        selector1 = Selector(text=response1.text)
        authenticity_token = selector1.xpath('//input[@name="authenticity_token"]/@value').extract()[0]
        ui_metric_response = self.session.get(url='https://twitter.com/i/js_inst?c_name=ui_metrics')
        selector_ui = Selector(text=ui_metric_response.text)
        ui_metric = selector_ui.re('return ({\'rf\'\:\{.*?\}\,\'s\'\:\'.*?\'\})')[0]
        print ui_metric

        postdata={
            'session[username_or_email]':username,
            'session[password]':password,
            'return_to_ssl':'true',
            'scribe_log':'',
            'redirect_after_login':'/',
            'authenticity_token':str(authenticity_token),
            'ui_metrics':str(ui_metric),
        }


        return postdata

    # def _get_user_from_exisitedcookie(self,):
    #     with open(self.basic_file+'cookie/LWPcookie/'+self.name,'r') as f:
    #         cookielist=pickle.load(file=f)
    #
    #     for onecookie in cookielist:
    #         self.cookie.set_cookie(onecookie)

    def _update_authenticity_token(self):
        # responseauthorkey=self.session.get(url='http://www.twitter.com', headers=self.headers,proxies=self.proxy_dict,cookies=self.cookie)
        responseauthorkey=self.session.get(url='http://www.twitter.com')
        selector1=Selector(text=responseauthorkey.text)
        self.authenticity_token=selector1.xpath('//input[@name="authenticity_token"]/@value').extract()[0]
        self.mainpagehtml=responseauthorkey.text

    def _get_replyPostdata(self,content,postUrl):
        postid=postUrl.split('status/')[1].strip('/')
        postdata={
            'authenticity_token':self.authenticity_token,
            'auto_populate_reply_metadata':'true',
            'batch_mode':'off',
            'in_reply_to_status_id':postid,
            'is_permalink_page':'true',
            'place_id':'',
            'status':content,
            'tagged_users':'',
            'weighted_character_count':''
        }
        return postdata

    def _get_cookie_pickle(self):
        cookielist = []
        try:
            for onecookie in self.cookie:
                cookielist.append(onecookie)
            cookielistdump=pickle.dumps(cookielist)
        except Exception as e:
            print e
        return cookielistdump


    def _create_UesrCookie_from_remoteData(self):
        # cookielist=pickle.loads(self.cookie_raw)
        #因为cookie类型改了


        cookielist=[]
        cookie_remote=json.loads(self.cookie_raw)
        for one_cookie in cookie_remote:
            cookie1=get_cookie_from_dict(one_cookie)
            cookielist.append(cookie1)


        for onecookie in cookielist:
            self.cookie.set_cookie(onecookie)

    def _add_proxy_to_selenium(self,proxy=None):
        if not proxy:
            myProxy = self.link_ip+':'+self.link_port
        else:
            myProxy=proxy
        options = webdriver.ChromeOptions()
        desired_capabilities = options.to_capabilities()
        desired_capabilities['proxy'] = {
            "httpProxy": myProxy,
            "ftpProxy": myProxy,
            "sslProxy": myProxy,
            "noProxy": None,
            "proxyType": "MANUAL",
            "class": "org.openqa.selenium.Proxy",
            "autodetect": False
        }
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
        return driver












# if __name__ == '__main__':
#     thisclass=twitter(account='mio1650392zhi@163.com',link_ip='192.168.6.7',link_port='8118')
#     thisclass.login(username='mio1650392zhi@163.com',password='ww13552')
#     # thisclass.get_exisitedUser_and_authenticity()
#
#     thisclass.publish_post(content='我会中文哦！')
#     # thisclass.reply_post(content='hi,hiiiiiiiiiiiii!',postUrl='https://twitter.com/metmuseum/status/960792691549396992')
#     # thisclass.thumb_up(thumbumurl='https://twitter.com/TEDTalks/status/960686589331505152')
#     # thisclass.share(shareposturl='https://twitter.com/warriors/status/960681895905210369',content='hi,the first share')


if __name__ == '__main__':
    data_geted={
        # 'name':'mio1650392zhi@163.com',
        'password':'ww13552',
        'link_ip':'192.168.6.8',
        'link_port':'8118',
        'link_id':1,
        'platform':'twitter',
        'content':'this is content',
        'type':'评论',
        'url':'https://twitter.com/SrBachchan/status/961864009166209024',
        'userId':1,
        'account':'mio1650392zhi@163.com',
        'account_id':1,
        'cookie':'',
        'guidance_id':3
    }
    thisclass=twitter(**data_geted)
    # thisclass.login_with_selenium()
    thisclass.get_user_cookie_local()

    # thisclass.get_exisitedUser_and_authenticity()
    thisclass.reply_post(content='wish healthy with you!',postUrl='https://twitter.com/ColorsEffect/status/950795743979126784')
    # thisclass.publish_post(content='报到一下')
    # thisclass.thumb_up(thumbumurl='https://twitter.com/warriors/status/961833343141666817')