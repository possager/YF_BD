from selenium import webdriver



chreomdriver=webdriver.Chrome()




cookielist1=[
    {u'domain': u'.baidu.com', u'name': u'H_PS_PSSID', u'value': u'1461_21095_22074', u'path': u'/', u'httpOnly': False, u'secure': False},
    {u'domain': u'.baidu.com', u'secure': False, u'value': u'AE85147EDD94C362BE79B22049B2EBF3:FG=1', u'expiry': 3665640270.078902, u'path': u'/', u'httpOnly': False, u'name': u'BAIDUID'},
    {u'domain': u'.baidu.com', u'secure': False, u'value': u'1518156624', u'expiry': 3665640270.078972, u'path': u'/', u'httpOnly': False, u'name': u'PSTM'},
    {u'domain': u'.baidu.com', u'secure': False, u'value': u'AE85147EDD94C362BE79B22049B2EBF3', u'expiry': 3665640270.078944, u'path': u'/', u'httpOnly': False, u'name': u'BIDUPSID'},
    {u'domain': u'www.baidu.com', u'name': u'BD_HOME', u'value': u'0', u'path': u'/', u'httpOnly': False, u'secure': False},
    {u'domain': u'www.baidu.com', u'secure': False, u'value': u'12314753', u'expiry': 1519020623, u'path': u'/', u'httpOnly': False, u'name': u'BD_UPN'}
]



for onecookie in cookielist1:
    chreomdriver.add_cookie(onecookie)