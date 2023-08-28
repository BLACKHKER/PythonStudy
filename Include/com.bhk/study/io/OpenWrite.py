'''
@Author  ：BLACKHKER
@Date    ：2023/8/28 10:32
@File    ：OpenWrite.py
@Description: 读文件操作(JavaIO流)
@Version 1.0
'''

'''======================================写入文件(重写)==========================================='''
# 打开/创建文件用w模式打开
file = open("D:\logs\writeData.txt", "w", encoding="UTF-8")
# 写入缓存
file.write("Success!")
# 写入硬盘
file.flush()
file.close()

'''======================================写入文件(追加)==========================================='''
# 追加文件用a模式打开
file = open("D:\logs\writeData.txt", "a", encoding="UTF-8")
# 写入缓存
file.write("Success!")
# 写入硬盘
file.flush()
file.close()