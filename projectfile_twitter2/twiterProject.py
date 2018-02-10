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




class twitter:
    def __init__(self,platform=None,content=None,password=None,type=None,link_ip=None,
                 link_port=None,url=None,userId=None,account=None,
                 account_id=None,cookie=None,link_id=None,title=None):
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

    def login(self,username=None,password=None):
        if username:
            username=self.name
        if password:
            password=self.password


        postdata=self._get_login_postdata(username=username,password=password)
        print postdata
        loginresponse=self.session.post(url='https://twitter.com/sessions',data=postdata,headers=self.headers)
        selector2=Selector(text=loginresponse.text)
        self.mainpagehtml=loginresponse.text#因为主页中有很多需要的值，比如后边点赞需要用到的js。
        self.authenticity_token = selector2.xpath('//input[@name="authenticity_token"]/@value').extract()[0]

        print loginresponse.status_code

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

        response_post=self.session.post(url='https://twitter.com/i/tweet/create',headers=headers1,data=postdata)
        print response_post.text

    def reply_post(self,content=None,postUrl=None):
        if not content:
            content=self.content
        if not postUrl:
            postUrl=self.url


        postdata=self._get_replyPostdata(content=content,postUrl=postUrl)
        posturl='https://twitter.com/i/tweet/create'

        headers1 = {
            # ':authority':'twitter.com',
            # ':method':'POST',
            # ':path':'/i/tweet/create',
            # ':scheme':'https',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-length': '',
            'origin': 'https://twitter.com',
            'referer': 'https://twitter.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-twitter-active-user': 'yes'
        }

        replyresponse=self.session.post(url=posturl,data=postdata,headers=headers1)
        print replyresponse.text

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
        cookielistpickle=self._get_cookie_pickle()
        post_cookie_dict={
            'cookie':cookielistpickle,
            'account_id':self.account_id,
            'link_id':self.link_id
        }

        cookieupdate_url='http://localhost:8081/action/cookie_update'

        self.session.post(url=cookieupdate_url,data=post_cookie_dict)

    def create_usercookie_from_remotedata(self):
        self._create_UesrCookie_from_remoteData()
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
        responseauthorkey=self.session.get(url='http://www.twitter.com', headers=self.headers)
        selector1=Selector(text=responseauthorkey.text)
        self.authenticity_token=selector1.xpath('//input[@name="authenticity_token"]/@value').extract()[0]
        self.mainpagehtml=responseauthorkey.text

    def _get_replyPostdata(self,content,postUrl):
        postid=postUrl.split('status/')[1]
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
        cookielist=pickle.loads(self.cookie_raw)
        for onecookie in cookielist:
            self.cookie.set_cookie(onecookie)











if __name__ == '__main__':
    thisclass=twitter(account='mio1650392zhi@163.com',link_ip='192.168.6.7',link_port='8118')
    thisclass.login(username='mio1650392zhi@163.com',password='ww13552')
    # thisclass.get_exisitedUser_and_authenticity()

    thisclass.publish_post(content='我会中文哦！')
    # thisclass.reply_post(content='hi,hiiiiiiiiiiiii!',postUrl='https://twitter.com/metmuseum/status/960792691549396992')
    # thisclass.thumb_up(thumbumurl='https://twitter.com/TEDTalks/status/960686589331505152')
    # thisclass.share(shareposturl='https://twitter.com/warriors/status/960681895905210369',content='hi,the first share')