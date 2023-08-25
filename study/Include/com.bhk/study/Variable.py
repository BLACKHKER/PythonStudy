# 变量作用域Demo
def funcTest():
    global num
    num = 1
funcTest()
print(num)