'''
提供对pymssql的简单封装
希望能提供一个可以快速操作数据库的方式
'''
import pymssql

'''
主机地址，用户名，密码，数据库
'''
HOST = USER = PASSWORD = DATABASE = None

def exsql(sql):
    '''
    执行指定的SQL语句返回结果集
    注意：需要提前配置全局变量，host,user,password,database
    '''
    # 创建连接
    conn = pymssql.connect(host=HOST, user=USER,
                           password=PASSWORD, database=DATABASE)
    # 打开游标
    cur = conn.cursor()

    if not cur:
        raise Exception('数据库连接失败，请检查数据库连接配置.')

    # 执行SQL语句
    cur.execute(sql)

    # 返回结果集
    return cur.fetchall()
