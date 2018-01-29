import pickle
import cookielib
import requests




def visit_page_with_cookie_picked():
    session=requests.session()
    with open('/media/slience-liang/3804CCCA04CC8C76/project_2018/YF_BD/cookies/baidu_lognin','r+') as f:
        # _cookie_pick=f.read()
        # cookie_from_pickled=pickle.dumps(_cookie_pick)
        # print type(cookie_from_pickled)
        # print cookie_from_pickled
        this_cookiejar=cookielib.MozillaCookieJar()
        cookie_pickle=pickle.load(f)

        print cookie_pickle
        cookie_str_in_headers = ''
        for i in cookie_pickle:
            name=i['name']
            value=i['value']
            print name
            print value
            cookie_str_in_headers+=name+'='+value+';'


        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.baidu.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        }
        headers['Cookie']=cookie_str_in_headers
        return headers




def get_web_page():
    headers=visit_page_with_cookie_picked()
    response=requests.get(url='https://www.baidu.com',headers=headers)
    # print response.text
    # print response.cookies
    del headers['Host']
    response=requests.get(url='https://tieba.baidu.com/index.html',headers=headers)
    # print response.text
    response2=requests.get(url='https://tieba.baidu.com/p/5521860466',headers=headers)
    print response2.text




if __name__ == '__main__':
    # visit_page_with_cookie_picked()
    get_web_page()