import pickle
import requests
from selenium import webdriver
from scrapy.selector import Selector
import time
import json
import sre_compile
from socket_function import *





with open('F:/project_2018/YF_BD/cookies/forum_data_info', 'r') as f:
    response1=pickle.load(file=f)

print response1.text
url = 'http://tieba.baidu.com/p/5465046117'
data = 'hahaheheheihei'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'Host': 'tieba.baidu.com',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}



# username='somepython'
# password='ll13629056300'
#
#
# driver=webdriver.Chrome()
# driver.get(url='https://www.baidu.com')
#
# login_botton=driver.find_elements_by_xpath('//div[@id="u1"]/a[@name="tj_login"]')
# print login_botton
# login_botton[0].click()
#
# time.sleep(3)
# driver.find_element_by_xpath('//p[@class="tang-pass-footerBarULogin"]').click()
# time.sleep(3)
#
# input_name = driver.find_element_by_xpath('//input[@class="pass-text-input pass-text-input-userName"]')
# input_name.send_keys(username)
#
# input_pwd = driver.find_element_by_xpath('//input[@id="TANGRAM__PSP_10__password"]')
# input_pwd.send_keys(password)
#
# driver.find_element_by_xpath('//input[@class="pass-button pass-button-submit"]').click()
# time.sleep(10)
# driver.find_element_by_xpath('//input[@class="pass-button pass-button-submit"]').click()
# cookies = driver.get_cookies()

with open('F:/project_2018/YF_BD/cookies/baidu_login', 'r+') as f:
    cookies = pickle.load(f)
#
Cookie_str = ''

for one_cookie in cookies:
    name = one_cookie['name']
    value = one_cookie['value']
    string1 = name + '=' + value + ';'

    Cookie_str += string1

print Cookie_str

headers['Cookie'] = Cookie_str

response1 = requests.get(url=url,headers=headers,allow_redirects=False)


selector1=Selector(text=response1.text)
print selector1.xpath('//script[contains(text(),"var topic_thread")]').re(' data \: \{(.*?)\}')
result= selector1.xpath('//script[contains(text(),"var topic_thread")]').re('.*kw:(.*?)\,.*ie:(.*?)\,.*?rich_text:(.*?)\,.*?floor_num:(.*?)\,.*?fid:(.*?)\,.*?tid:(.*?)\,')
tbs= selector1.xpath('//script[contains(text(),"var PageData")]').re('"tbs"  \: "(.*?)"\,')

#ie,rich_text,floor_num,fid,tid
# for i in result:
#     print i


data = {'tbs': tbs[0]}
datajson = json.dumps(data)
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(('127.0.0.1', 23456))
sendmsg(datajson, sock=socket1)
data = recvmsg(sock=socket1)
print data
bsk_dict=json.loads(data)


post_data={
    'ie':'utf-8',
    'kw':result[0],
    'rich_text':'1',
    'floor_num':'94',
    'fid':result[-2],
    'tid':result[-1],
    'tbs':tbs[0],
    'content':'mark123',
    'mouse_pwd_t':'15169009770400',#str(int(time.time()*1000)),
    '_type_':'reply',
    'basilisk':'1',
    'files':[],
    '_BSK':bsk_dict['bsk']
}

print post_data


post_url='https://tieba.baidu.com/f/commit/post/add'

with open('F:/project_2018/YF_BD/cookies/baidu_login','r+') as f:
    cookies=pickle.load(f)

Cookie_str=''
for one_cookie in cookies:
    name = one_cookie['name']
    value = one_cookie['value']
    string1 = name + '=' + value + ';'

    Cookie_str += string1

print Cookie_str

headers1={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 OPR/50.0.2762.67',
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
}
headers1['Cookie']=Cookie_str
reponse2=requests.post(url=post_url,headers=headers1,data=post_data)

print reponse2.text



# tbs="f94fd8ccc33a23e71516760935"
#
#
#
# class a:
#     def __init__(self):
#         a = "omzVouOACqkNljzDbdOB"
#         MAP="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/<$+-%>{:* \,}[^=_~&](\")"
#
#
# def b():
#     b.B='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/<$+-%>{:* \\,}[^=_~&](")   '
#
