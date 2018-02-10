#_*_coding:utf-8_*_
import requests
import json
from baiduloginer import baiduloger
import time







url1='http://192.168.6.145:8081/action/mission'
data={
    'platform':'今日头条'
}




def service_getTask():
    while True:
        response1=requests.post(url1,data=data)
        print response1.text
        time.sleep(1)
        datajson=json.loads(response1.text)
        print datajson


        if datajson['data']:

            data=datajson['data']

            thisclass=baiduloger(**data)


            # platform=datajson['data']['platform']
            # content=datajson['data']['content']
            # # title=datajson['data']['title']
            # password=datajson['data']['password']
            # type=datajson['data']['type']
            # link_ip=datajson['data']['link_ip']
            # link_port=datajson['data']['link_port']
            # url=datajson['data']['url']
            # userId=datajson['data']['userId']
            #
            # account=datajson['data']['account']
            # account_id=datajson['data']['account_id']
            cookie=datajson['data']['cookie']
            # link_id=datajson['data']['link_id']


            if cookie:
                thisclass.create_usercookie_from_remotedata()
                result=execute_task(data=data,twitterInstance=thisclass)
            else:
                try:
                    thisclass.login_with_selenium()
                except Exception as e:
                    print e
                    return False
                thisclass.save_user_Cookie()
                result=execute_task(data=data,twitterInstance=thisclass)

            #怎么处理这个result,cookie失效的样子是什么样子的。。。。。。。目前没有碰到cookie失效的情况。


            thisclass.reply_post()
            thisclass.share()



        time.sleep(30)



def execute_task(data,twitterInstance):
    taskType=data['type']
    if taskType=='评论':
        result=twitterInstance.reply_post()
    elif taskType=='转发':
        result=twitterInstance.share()
    elif taskType=='发帖':
        result=twitterInstance.publish_post()
    elif taskType=='点赞':
        result=twitterInstance.thumb_up()
    else:
        return False

    return result