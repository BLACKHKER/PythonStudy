import json
from datetime import date, datetime
from pymongo import MongoClient

# 自定义转换器，继承JSON类
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

# MongoDB连接信息
mongo_host = 'localhost'  # MongoDB服务器地址
mongo_port = 27017  # MongoDB端口号
database_name = 'JIAOYI-TEST'  # 数据库名称
collection_name = 'ocean'  # 集合名称

# 建立MongoDB连接
client = MongoClient(mongo_host, mongo_port)
db = client[database_name]
collection = db[collection_name]

cursor = collection.find({}, {"_id": 0}).sort("time", -1).limit(100)

# 打开文件exportData.txt，w模式为文件不存在则创建新文件
file = open("D:\logs\exportData.txt", "w")

for document in cursor:
    # print(document)

    # 将文档类型转换为字符串类型
    documentStr = json.dumps(document, cls=ComplexEncoder)
    print(documentStr)

    # 写入一行数据
    file.write(documentStr + "\n")

# 关闭文件
file.close()

# 关闭MongoDB连接
client.close()

# 保存完毕
print("最新100条数据导出完毕")
