'''
@Author  ：BLACKHKER
@Date    ：2023/8/25 15:37
@File    ：Dictionary.py
@Description: 字典Demo
@Version 1.0
'''
# 定义空字典
# dic = {}
# dic = dict()
# dic = {"key1": value2, "key2": value2}

# 遍历字典
myDic = {"1": 10, "2": 20, "3": 30}
# 根据key遍历
keys = myDic.keys()
for key in keys:
    print(myDic[key])

# 根据字典遍历
for key in myDic:
    print(myDic[key])
