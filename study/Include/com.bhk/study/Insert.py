import os
from pymongo import MongoClient
from datetime import datetime

# MongoDB连接信息
mongo_host = 'localhost'  # MongoDB服务器地址
mongo_port = 27017  # MongoDB端口号
database_name = 'JIAOYI-TEST'  # 数据库名称
collection_name = 'ocean'  # 集合名称

# 建立MongoDB连接
client = MongoClient(mongo_host, mongo_port)
db = client[database_name]
collection = db[collection_name]

# 文件夹路径Mo
folder_path = 'D:/MongoTestData'  # 将此处的路径替换为你的文件夹路径

# 遍历文件夹内的所有txt文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)

        # 读取txt文件内容
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 批量插入的文档列表
        documents = []

        # 处理每一行数据并添加到文档列表
        for line in lines:
            data = line.split('\t')

            # 提取数据项
            # time = datetime.strptime(data[0][:14], '%Y%m%d%H%M%S').isoformat()
            time = datetime.strptime(data[0][:14], '%Y%m%d%H%M%S')
            sample = int(data[0][14:17])
            channel1 = float(data[1])
            channel2 = float(data[2])
            compass = int(data[3])
            number = int(data[4])

            # 构造文档
            document = {
                'time': time,
                'sample': sample,
                'channel1': channel1,
                'channel2': channel2,
                'compass': compass,
                'number': number
            }

            # 添加文档到列表
            documents.append(document)

        # 批量插入文档
        if documents:
            collection.insert_many(documents)

        # 显示正在处理的文件名
        print(f"正在处理文件: {file_name}")

# 关闭MongoDB连接
client.close()

# 提示文件入库完毕
print("所有文件入库完毕")
