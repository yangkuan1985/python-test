from utils import mssql, pyredis, mongodb
from urllib import request

response=request.urlopen("http://www.baidu.com")
print(response.read().decode("utf-8"))

'''
#mongo演示
mongodb.HOST = "192.168.158.130"
mongodb.PORT = 27017
mongodb.DB = "test"
mongodb.COLLECTION = "testset"

for item in mongodb.find():
    for (key, value) in item.items():
        print(key, value)

#redis演示
pyredis.HOST = "192.168.158.130"
pyredis.PORT = 6379

pyredis.setvalue("key", "ewfwef323")
pyredis.getvalue("key")

#SQL SERVER演示
mssql.HOST = "127.0.0.1:62331"
mssql.USER = "sa"
mssql.PASSWORD = "1"
mssql.DATABASE = "xindata"

for row in mssql.exsql("select * from users"):
    for col in row:
        print(col)

'''
