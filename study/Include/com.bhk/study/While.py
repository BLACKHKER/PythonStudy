# While循环Demo
# age = 10
# while age < 100:
#     age += 1
# print(age)

# 计算从1加到100的和
# sum = 1
# num = 1
# while num < 100:
#     num += 1
#     sum += num
# print(sum)

# 九九乘法表
i = 1
j = 1
while i <= 9:
    while j <= i:
        print(f"{j}*{i}={i * j}\t", end='')
        j += 1
    print()
    i += 1
    j = 1