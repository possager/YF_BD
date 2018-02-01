# _*_coding:utf-8_*_
import socket
import requests
from selenium import webdriver
import time
import pickle
from multiprocessing import Process
from socket_function import *
import json

basic_file = 'cookie/Selenium_cookie/'


def login():
    username = 'somepython'
    password = 'll13629056300'

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

    element_publish_text = driver.find_element_by_xpath('//div[@id="ueditor_replace"]')
    element_publish_text.send_keys('shuishuijingyan')
    time.sleep(2)
    publish_button = driver.find_element_by_xpath(
        '//div[@class="poster_component editor_bottom_panel clearfix"]/div[@class="j_floating"]/a')
    publish_button.click()

    cookies = driver.get_cookies()

    with open(basic_file + 'somepython', 'w+') as f:
        pickle.dump(obj=cookies, file=f)

    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_port=23456
    while True:
        try:
            socket1.bind(('127.0.0.1', socket_port))
            break
        except:
            socket_port+=1

    socket1.listen(5)
    while True:
        try:

            conn, addr = socket1.accept()
            data = recvmsg(conn=conn)

            data_dict = json.loads(data)

            tbs = data_dict['tbs']

            script = '''
            var a=function(){var t = {};
                                window._BSK.a("omzVouOACqkNljzDbdOB", {
                                    IN: {tbs:"%s"},
                                    OUT: t
                                }); return t.data};

            return a();

            ''' % (tbs)
            # print script
            #omzVouOACqkNljzDbdOB

            BSK = driver.execute_script(script)

            print BSK

            bsk_data = {
                'bsk': BSK
            }
            bsk_data_json = json.dumps(bsk_data)
            sendmsg(bsk_data_json, conn=conn)

            conn.close()
            print data
        except Exception as e:
            print e


if __name__ == '__main__':
    # socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # socket1.bind(('127.0.0.1',23456))
    # socket1.listen(5)
    # while True:
    #     conn,addr=socket1.accept()
    #     data=recvmsg(conn=conn)
    #     print data
    #     print type(data)
    #     conn.close()
    login()