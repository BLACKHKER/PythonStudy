import random

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