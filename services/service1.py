import requests
from projectfile_BD import baidu_Selenium_loginer
from projectfile_BD import baiduloginer

from projectfile_twitter import twiterProject



def listen_service(*args,**kwargs):
    print args
    print '\n\n\n'
    print kwargs




def listen_service2(key1=None,key2=None,key3=None,key4=None):
    print key1
    print key2
    print key3
    print key4

list1=[1,2,3,4,5,6]


dict1={
    'name':'hi',
    'age':12,
    'famale':True
}
# listen_service(1,2,3,4,5,name=dict1['name'],age=dict1['age'])

dict2={
    'key1':1,
    'key2':2,
    'key3':3,
    'key4':4
}

listen_service2(**dict2)