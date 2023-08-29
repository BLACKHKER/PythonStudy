"""
@Author  ：BLACKHKER
@Date    ：2023/8/29 10:37
@File    ：Class.py
@Description: 类Demo
@Version 1.0
"""


class Person:
    id = None
    name = None

    def sayHello(self):
        print(f"你好，我是{self.name}")

    def sayMessage(self, message):
        print(f"你好，我是：{self.name}，这个问题:{message}需要解决一下")


person = Person()
person.id = 1
person.name = "刘备"
person.sayHello()
person.sayMessage("index of outBounds")
