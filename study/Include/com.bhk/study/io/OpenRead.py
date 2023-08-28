'''
@Author  ：BLACKHKER
@Date    ：2023/8/25 17:53
@File    ：Open.py
@Description: 读文件操作(JavaIO流)
@Version 1.0
'''
import time

'''======================================read()==========================================='''
# 读取某数量的字符
# 从文件中读取1的长度(单位字节)
# file = open("D:\logs\exportData.txt", "r", encoding="UTF-8")
# context = file.read(1)
# print(context)

# 如果没有传入num，就表示读取文件中的所有数据
# file = open("D:\logs\exportData.txt", "r", encoding="UTF-8")
# context = file.read()
# print(context)

'''======================================readline()==========================================='''
# 以只读方式打开文件
# file = open("D:\logs\exportData.txt", "r", encoding="UTF-8")
# context = file.readline()
# print(context)
# file.close()

'''======================================for==========================================='''
# for循环打开文件
# 基础
# file = open("D:\logs\exportData.txt", "r", encoding="UTF-8")
# for line in file:
#     print(line)
# 测试打开文件进程占用
# time.sleep(50000)
# file.close()

# 简写
# for line in open("D:\logs\exportData.txt", "r", encoding="UTF-8"):
#     print(line)

'''======================================with open==========================================='''
# with open("D:\logs\exportData.txt", "r", encoding="UTF-8") as file:
#     for line in file:
# 	    print(line)
