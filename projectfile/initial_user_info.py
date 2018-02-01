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
    username = 'zengl7917@163.com'
    password = 'xiaosi777'

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
    try:
        #可能没有验证码，没有验证码的话这里就有可能出错。
        driver.find_element_by_xpath('//input[@class="pass-button pass-button-submit"]').click()
    except Exception as e:
        print e

    time.sleep(2)
    driver.get(url='http://tieba.baidu.com/p/5465046117')

    # element_publish_text = driver.find_element_by_xpath('//div[@id="ueditor_replace"]')
    # element_publish_text.send_keys('shuishuijingyan')
    time.sleep(2)
    # publish_button = driver.find_element_by_xpath(
    #     '//div[@class="poster_component editor_bottom_panel clearfix"]/div[@class="j_floating"]/a')
    # publish_button.click()

    cookies = driver.get_cookies()

    with open(basic_file + username, 'w+') as f:
        pickle.dump(obj=cookies, file=f)



if __name__ == '__main__':
    login()