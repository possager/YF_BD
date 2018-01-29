#_*_coding:utf-8_*_
import execjs






a_dict={
    "IN":{'tbs':'1796da2383a8d7601516771376'},
    'OUT':{}
}
b_dict="omzVouOACqkNljzDbdOB"


with open('F:/project_2018/YF_BD/javascript/VM180.js') as f:
    java_script= f.read()
    java_exer=execjs.compile(java_script)

    print java_exer.call('a',b_dict,a_dict)
    # print java_exer.call('a',1,2)