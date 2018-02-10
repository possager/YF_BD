import requests





proxy_dict={
    'http':'http://'+'192.168.6.8:8118',
    'https':'https://'+'192.168.6.8:8118'
}

session1=requests.session()
session1.proxies=proxy_dict


respons2=session1.get(url='http://twitter.com')
print respons2.text
print respons2.status_code