'''
提供对redis的简单封装
通过简单的配置，可以快速的操作redis
'''

import redis

'''
主机，端口
'''
HOST = PORT = None

def setvalue(key, value):
    '''
    将key的值设置为value
    '''
    getredis().set(key, value)


def getvalue(key):
    '''
    获取key的值
    '''
    return getredis().get(key)

def getredis():
    '''
    获取redis client
    '''
    return redis.Redis(HOST, PORT)
