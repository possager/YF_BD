#_*_coding:utf-8_*_
import requests
import json





url1='http://192.168.6.145:8081/action/mission'
data={
    'platform':'今日头条'
}

response1=requests.post(url1,data=data)
print response1.text


datajson=json.loads(response1.text)
print datajson

if datajson['data']:

    platform=datajson['data']['platform']
    content=datajson['data']['content']
    # title=datajson['data']['title']
    password=datajson['data']['password']
    type=datajson['data']['type']
    link_ip=datajson['data']['link_ip']
    link_port=datajson['data']['link_port']
    url=datajson['data']['url']
    userId=datajson['data']['userId']

    account=datajson['data']['account']
    account_id=datajson['data']['account_id']
    cookie=datajson['data']['cookie']
    link_id=datajson['data']['link_id']


    if cookie:
        print 'has cookies,用cookie去操作把'
    else:
        print '没有用户信息，自己去生成一个哦！'

    print datajson['data']


# if platform==''