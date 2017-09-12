'''
对pymongo的简单封装
提前配置使用到的参数即可免去复杂的重复操作
'''

import pymongo

'''
数据库名,集合名，主机，端口
'''
DB = COLLECTION = HOST = PORT = None

def find():
    '''
    返回指定集合中的所有存储
    '''
    return getcollection().find()

def getcollection():
    '''
    获取mongo集合
    '''
    client = getclient()

    if not DB:
        raise Exception("未配置数据库")

    if not COLLECTION:
        raise Exception("未配置集合")

    return client[DB][COLLECTION]

def getclient():
    '''
    返回mongodb client
    '''
    if not HOST:
        raise Exception("未配置主机")

    if not PORT:
        raise Exception("未配置端口号")

    return pymongo.MongoClient(HOST, PORT)
