#_*_coding:utf-8_*_

import requests
import pickle
import cookielib
from scrapy.selector import Selector




session1=requests.session()
cookiejar1=cookielib.LWPCookieJar()


headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
}




basic_file='F:/project_2018/YF_BD/projectfile_twitter/'




cookielist=[]
with open(basic_file + 'cookie/LWPcookie/' + 'mio1650392zhi@163.com' + '2', 'r') as f:
    cookielist1 = pickle.load(f)

    for onecookie in cookielist1:
        cookiejar1.set_cookie(onecookie)
    # self._update_authenticity_token()



proxy_dict={
    'https':'https://192.168.6.6:8118',
    'http':'http://192.168.6.6:8118'

}


session1.cookies=cookiejar1
session1.headers.update(headers)
session1.proxies=proxy_dict



# response1=session1.get(url='http://twitter.com')
# print response1.text


cookiestr='personalization_id="v1_p0E5uvXnkoBU3+Pjso08Lg=="; guest_id=v1%3A151824523067929295; external_referer=padhuUp37zhCDepgXWiVsH%2FCSp%2BRC3Dym8jYDs6cqwjdmlSHqMfBEAa0leuXWwFr5zlvVk4mG41eNfOoyiN8lPVizzrdyo4dCVi%2BhkoCf4HXInw9vDCjRtJFQ2NUZxVkuMfvU%2FPxwoeRhgMAsIHMQ11bzmwLgumw|0|8e8t2xd8A2w%3D; ct0=39c419687ffed121b7e8b7a033df7e3e; _ga=GA1.2.1623788460.1518245232; _gid=GA1.2.909735917.1518245232; _gat=1; ads_prefs="HBERAAA="; kdt=FVBnw8hk889Gniv5lo0ZsSLw3QEvELR5JyMVXyT4; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCFm4d35hAToMY3NyZl9p%250AZCIlNWZjM2U3OTRiNTlhZDk1MzBlOWQwYzQ5NTU1Nzk0N2M6B2lkIiU4MWI0%250AYzE5NjNlNDE2NDFhZDIxMDFkYWM0ZjA0M2YyODoJdXNlcmwrCQAQ1FniWQUN--bd12844f1916bde19c8c9882c939273fdad6274b; remember_checked_on=0; twid="u=938254926081167360"; auth_token=fd957096e2aa135c7baf9eb76ee6b0f3925acdd2; lang=zh-cn'
headers['Cookie']=cookiestr



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


headers1['Cookie']=cookiestr

headers2={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'cache-control':'max-age=0',
    'referer':'https://twitter.com/',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
}

headers2['Cookie']=cookiestr







response2=requests.get(url='http://twitter.com',headers=headers2)
print response2.status_code
print response2.text


selelctor1=Selector(text=response2.text)

authertoken= selelctor1.xpath('//input[@name="authenticity_token"]/@value')[0].extract()



postdata={
            'authenticity_token':authertoken,
            'auto_populate_reply_metadata':'true',
            'batch_mode':'off',
            'in_reply_to_status_id':'962195881045975042',
            'is_permalink_page':'true',
            'place_id':'',
            'status':'今天好无聊',
            'tagged_users':'',
            'weighted_character_count':''
        }

posturl = 'https://twitter.com/i/tweet/create'

# reponse_post=requests.post(url=posturl,data=postdata,headers=headers2)
# print reponse_post.text
# print reponse_post.status_code
response3=session1.post(url=posturl,data=postdata,headers=headers2)
print response3.text
print response3.status_code