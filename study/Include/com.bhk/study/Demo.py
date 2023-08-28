import random

"""
    公司账户余额有一万元，给20名员工发工资，员工没人领取工资1000元
    财务需要判断该员工的绩效(随机数)，低于5不发工资
    工资发完则结束发工资
"""
# money = 10000
# for i in range(1, 21):
#     # 判断薪水是否足够
#     if money >= 1000:
#         score = random.randint(1, 10)
#         # 判断绩效
#         if score > 5:
#             money -= 1000
#             print(f"向员工{i}发放工资1000元，余额{money}元")
#         else:
#             print(f"员工{i},绩效分{score},低于5,不发工资！")
#     else:
#         print("没钱了！")
#         break

"""
    函数Demo，定义函数，接受一个参数体温，在函数内进行体温判断(正常范围：小于37.5度)
    输出以下内容：您的体温是：37.5度，体温正常请进/体温不正常需要隔离！
"""
# def temperature(number):
#     if number <= 37.5 and number >= 36.1:
#         print(f"您的体温是{number}度，体温正常请进")
#     else:
#         print(f"您的体温是{number}，体温不正常，需要隔离！")
#
# number = input("请输入体温：")
# temperature(int(input("请输入体温：")))

'''
    读取文件统计字符出现次数
'''
with open("D:\logs\exportData.txt", "r", encoding="UTF-8") as f:
    count = 0
    for line in f:
        num = line.count("sample")
        count += num
        num = 0
        print(line)
print(f"sample的出现次数是：{count}次")
