import cookielib
import requests




cookie_jar=cookielib.LWPCookieJar()


session1=requests.session()
session1.cookies=cookie_jar



headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host': 'tieba.baidu.com',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }


response1=session1.request(method='get',url='https://www.baidu.com',headers=headers)

response2=session1.request(method='get',url='http://tieba.baidu.com/p/5465046117?traceid=',headers=headers)

response3=session1.request(method='get',url='https://weibo.com')


response4=session1.request(method='get',url='https://www.csdn.net/')
for i in session1.cookies:
    print i


cookie_jar.save(filename='F:/project_2018/YF_BD/cookies/cookiejar')
session1.close()