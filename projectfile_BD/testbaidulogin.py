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
from selenium import webdriver

from selenium.webdriver.common.proxy import *
myProxy='192.168.6.8:8118'
options = webdriver.ChromeOptions()
desired_capabilities = options.to_capabilities()
desired_capabilities['proxy'] = {
    "httpProxy":myProxy,
    "ftpProxy":myProxy,
    "sslProxy":myProxy,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}
driver = webdriver.Chrome(desired_capabilities = desired_capabilities)
driver.get("http://www.youtube.com")