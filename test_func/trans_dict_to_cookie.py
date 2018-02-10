#_*_coding:utf-8_*_
import requests
import cookielib
import json
import pickle
from cookie_deal import get_cookie_from_dict
from selenium import webdriver




def test():

    cookiejar=cookielib.LWPCookieJar()
    with open('F:/project_2018/YF_BD/projectfile_BD/'+'cookie/Selenium_cookie/somepython','r') as f:

        cookielist=pickle.load(f)

    driver=webdriver.Chrome()


    cookiestr=''
    for onecookie in cookielist:
        # print onecookie
        _cookie=get_cookie_from_dict(onecookie)
        cookiejar.set_cookie(_cookie)
        # cookiestr+=onecookie['name']+'='+onecookie['value']+';'
        # print onecookie['name']
        print onecookie
        cookie_dict={
            'name':_cookie.name,
            'value':_cookie.value,
            # 'domain':_cookie.domain,
            # 'path':_cookie.path
        }


        # driver.add_cookie(cookie_dict)
        cookie_dict_example={
            'name':'name',
            'value':'value'
        }
        driver.add_cookie(cookie_dict_example)

    driver.get(url='http://www.baidu.com')



if __name__ == '__main__':
    test()