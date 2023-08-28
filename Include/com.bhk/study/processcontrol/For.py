# for循环Demo
# array = [1, 2, 3, 4, 5]
# for i in array:
#     print(i)
# print("Success!")

# 判断字符串中有几个a
# num = 0
# str = "panda is big animal"
# for i in str:
#     if (i == "a"):
#         num += 1
# print(f"该字符串中有{num}个a字符")

# 注意：for循环的临时变量是可以被循环体外部访问到的如下代码会打印两遍4
# i = 0
# for i in range(5):
#     print(i)
# print(i)

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        # if j <= i:
            print(f"{j}*{i}={i * j}\t", end='')
    print()