import requests
import pickle
from w3lib.url import urlsplit

def get_redict1():
    with open('F:/project_2018/YF_BD/cookies/response_one_forum', 'r') as f:
        response1=pickle.load(f)
    print type(response1)
    # return response1.headers['Location']
    print response1.headers
    print type(response1.headers)
    # if 'Set-Cookie' in response1.headers.keys:
    #     print response1.headers['Set-Cookie']
    # print dict(response1.headers)['Set-Cookie'].split(';')[0].split('=',1)
    print type(response1.headers['Set-Cookie'])



def dealing_response(url=None,headers=None):
    host=urlsplit(url=url).netloc
    headers['Host']=host
    response=requests.get(url=url,headers=headers,allow_redirects=False)
    if response.status_code==302:
        cookies=[]
        try:
            set_cookie=response.headers['Set-Cookie']
            cookie_pre=set_cookie.split(';')[0]
            name,value=cookie_pre.split('=')
            cookies.append([name,value])
        except Exception as e:
            print e


        return [False,response.headers['Location'],cookies]
    else:
        return [True,response]



def run():
    url = 'http://tieba.baidu.com/p/5465046117'
    data = 'hahaheheheihei'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host': 'tieba.baidu.com',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    with open('F:/project_2018/YF_BD/cookies/baidu_login', 'r+') as f:
        cookies = pickle.load(f)

    Cookie_str = ''

    for one_cookie in cookies:
        name = one_cookie['name']
        value = one_cookie['value']
        string1 = name + '=' + value + ';'

        Cookie_str += string1

    print Cookie_str

    headers['Cookie'] = 'BAIDUID=1D5ED363A508DECEC4B60CB9C049D03A:FG=1; BIDUPSID=1D5ED363A508DECEC4B60CB9C049D03A; PSTM=1516931991; HOSUPPORT=1; FP_UID=b90a98386223a190908c4aef82d88d1c; DVID=1516931998839%7Cc36c7aa9-8a99-46d1-98cf-3d3d59e0df75; UBI=fi_PncwhpxZ%7ETaKAU80BVgWLvSbCmUpPkzKXAGXT2o1q0aNUYl2ROACZhXEhzRKWMxyJOHCavt29mkHveOr; HISTORY=528f05b1c33f8cabd0c3e07df0520030429f; BDUSS=VnZG45RnZxQW1FY3VJOXB4cGRWdHpRQX5VMjNLWUhXfmMwTjJhbldlZXBHSkphQVFBQUFBJCQAAAAAAAAAAAEAAACPIk~Oc29tZXB5dGhvbgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKmLalqpi2paZ2; SAVEUSERID=c1709e40abb0ae6be37ab90b7ddd; USERNAMETYPE=1; PTOKEN=dfa70c9eb7988daa1d007e90ac607a1a; STOKEN=6a7fa4f1dc3c47975705d69de021858934879fb66081664ab0ad070cfe06b140; H_PS_PSSID=1456_21111_20697_20927'

    response1 = dealing_response(url=url, headers=headers)
    while not response1[0]:
        cookies2=response1[2]
        cookie_str2=''
        for one_cookie2 in cookies2:
            cookie_str2+=one_cookie2[0]+'='+one_cookie2[1]+';'

        headers['Cookie']+=cookie_str2

        response1=dealing_response(url=response1[1],headers=headers)
    print response1



if __name__ == '__main__':
    run()