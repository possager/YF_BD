from w3lib.url import urlsplit


url_string='https://passport.baidu.com/v3/login/api/auth/?tpl=tb&jump=&return_type=3&u=http%3A%2F%2Ftieba.baidu.com%2Fp%2F5465046117'

url_splited=urlsplit(url=url_string)

print url_splited.netloc