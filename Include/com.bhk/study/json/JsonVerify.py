"""
@Author  ：BLACKHKER
@Date    ：2023/8/28 14:22
@File    ：JsonVerify.py
@Description: Python格式化JSON字符串
@Version 1.0
"""

import json

# 数据格式化，列表嵌套字典转换JSON
# data = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]
# 将数据转换为JSON字符串，配置ensure_ascii不使用ASCII码转换中文
# jsonStr = json.dumps(data, ensure_ascii=False)
# String类型
# print(type(jsonStr))
# print(jsonStr)

# 字典转换JSON
# dic = {"name": "周杰伦", "addr": "台北"}
# jsonStr = json.dumps(dic, ensure_ascii=False)
# print(type(jsonStr))
# print(jsonStr)

# JSON字符串转换成Python数据类型(List)
# jsonStr = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]
# listA = list([{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}])
# print(type(listA))
# print(listA)

# JSON字符串转换成字典(dict)
jsonStr = {"name": "周杰伦", "addr": "台北"}
dictA = dict([{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}])
print(type(dictA))
print(dictA)
