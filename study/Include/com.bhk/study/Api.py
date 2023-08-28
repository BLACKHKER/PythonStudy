import random

"""============================================range()==================================================="""

# 从0开始，到num结束
# numsArray = range(10)
# for i in numsArray:
#     print(i)

# 从num1开始，到num2结束，不含num2本身
# numsArray = range(10,18)
# for i in numsArray:
#     print(i)

# 从num1开始，到num2结束，步长为num3
# numArray = range(4,10,2)
# for i in numArray:
#     print(i)

# 统计有几个偶数
# x = 1
# y = 100
# count = 0
# numsArray = range(x, y)
# for i in numsArray:
#     if (i % 2 == 0):
#         count += 1
# print(f"{x}到{y}有{count}个偶数")

"""============================================random()==================================================="""
# 随机从0-1选出一个浮点数
# f = random.random()
# print(f,type(f))

# 创建一个集合从集合中随机选取
# my_list = [1, 2, 3, 4, 5]
# random_choice = random.choice(my_list)
# print(random_choice)

# 随机打乱序列(集合)元素顺序
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)

# 生成一个位于指定范围的[最大值，最小值]中的随机浮点数
# random_float = random.uniform(1.0,5.0)
# print(random_float)

# 从总体 population 中随机选择 k 个不重复的元素作为样本，返回一个新的列表
my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 3)
print(random_sample)

"""============================================input()==================================================="""
# 从键盘接收数据
# 提前print打印提示语
print("你的名字是？")
name = input();
print(f"好的,{name}")

# 将提示语放到input方法中，作为参数，区别是没有换行
# name = input("你的名字是？\n");

print(f"好的，{name}")