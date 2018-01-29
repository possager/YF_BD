import cookielib




def get_cookie_from_dict(cookie_dict):

    standral_cookie_dict={

        'domain': '',
        'secure': False,
        'path_specified': True,
        # 'expires': '2019-01-29 01:40:02Z',
        'version': '0',
        'domain_initial_dot': True,
        'path': '/',
        'discard': False,
        'port_specified': False,
        'name':'',
        'value':'',
        'port':'',
        'domain_specified':'',
        'comment':'',
        'comment_url':'',
        'rest':'',
        'expires':0,

    }




    for cookie_name in cookie_dict.keys():
        if cookie_name=='path_spec':
            cookie_name='path_specified'
        if cookie_name=='domain_dot':
            cookie_name='domain_initial_dot'
        standral_cookie_dict[cookie_name]=cookie_dict[cookie_name]

    Cookie=cookielib.Cookie(**standral_cookie_dict)
    return Cookie



cookie_dict1={
    'name':'hello',
    'value':'hello'
}


cookie=get_cookie_from_dict(cookie_dict1)
cookie_lwp=cookielib.LWPCookieJar()
cookie_lwp.set_cookie(cookie)
print cookie_lwp
print cookie