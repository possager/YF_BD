import execjs
import requests
import cookielib
import time
import re




def get_gid_And_Callback():
    with open('F:/project_2018/YF_BD/javascript/'+'baidu_caculate_postdata.js','r+') as f:
        jsdata=f.read()
        javafunction=execjs.compile(jsdata)

    gid= javafunction.call('bd_gid','x')
    callbackname= javafunction.call('bd_callback','bd__cbs__')

    return {'gid':gid,'callback':callbackname}




def login():
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
    }


    session1=requests.session()
    cookiejar1=cookielib.LWPCookieJar()
    session1.cookies=cookiejar1
    session1.headers=headers

    response1=session1.get('http://www.baidu.com')
    print response1.text
    gid_cbk=get_gid_And_Callback()

    'https://passport.baidu.com/v2/api/?getapi&tpl=mn' \
    '&apiver=v3&tt=1517983215622&class=login&gid=C95CC6D-326D-43F4-85ED-7687BA0CD417&loginversion=v4&logintype=dialogLogin&traceid=&callback=bd__cbs__ulfy4j'

    url1='https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3&tt='+str(int(time.time()*1000))+'&class='+gid_cbk['gid']+'&loginversion=v4&logintype=dialogLogin&traceid=&callback='+gid_cbk['callback']

    responsee2=session1.get(url1)
    Re_find_token=re.compile('token\".*?\:.*?\"(.*?)\"')



    print str(Re_find_token.findall(responsee2.text)[0])

if __name__ == '__main__':
    login()