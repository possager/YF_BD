#_*_coding:utf-8_*_
import socket
import json

from protocol import *




def sendmsg(jsonMSG=None, conn=None, sock=None, addr=None):
    s = conn if conn else sock
    s.settimeout(20)
    len_of_data = len(jsonMSG)
    data_len_json = json.dumps({
        'len_data': len_of_data
    })
    # while True:#觉得这个while True，没有太大的意义
    s.sendall(data_len_json)
    data_resp = s.recv(1024)
    data_resp = json.loads(data_resp)
    if data_resp[MSG_TYPE] == STATUS_FINISH:
        pass

    while True:
        s.sendall(jsonMSG)
        data_resp = s.recv(1024)
        data_resp = json.loads(data_resp)
        if data_resp[MSG_TYPE] == STATUS_FINISH:
            break



def recvmsg(conn=None, sock=None, addr=None):
    s = conn if conn else sock
    s.settimeout(20)
    len_of_data = s.recv(1024)
    len_of_data = json.loads(len_of_data)
    data_finish = json.dumps({
        MSG_TYPE: STATUS_FINISH
    })
    s.sendall(data_finish)

    len_data = len_of_data['len_data']

    data = ''
    while True:
        _data = s.recv(1024)
        data += _data
        if len(data) >= len_data:
            break
    s.sendall(data_finish)

    return data


if __name__ == '__main__':
    data={'tbs':'1796da2383a8d7601516771376'}
    datajson=json.dumps(data)
    socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket1.connect(('127.0.0.1',23456))
    sendmsg(datajson,sock=socket1)
    data=recvmsg(sock=socket1)
    print data