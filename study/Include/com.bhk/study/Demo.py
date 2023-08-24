import random

"""
    公司账户余额有一万元，给20名员工发工资，员工没人领取工资1000元
    财务需要判断该员工的绩效(随机数)，低于5不发工资
    工资发完则结束发工资
"""
money = 10000
for i in range(1, 21):
    # 判断薪水是否足够
    if money >= 1000:
        score = random.randint(1, 10)
        # 判断绩效
        if score > 5:
            money -= 1000
            print(f"向员工{i}发放工资1000元，余额{money}元")
        else:
            print(f"员工{i},绩效分{score},低于5,不发工资！")
    else:
        print("没钱了！")
        break
