"""
@Author  ：BLACKHKER
@Date    ：2023/8/29 16:53
@File    ：Interface.py
@Description: 接口Demo
@Version 1.0
"""


# 空调类
class AC:
    def coolWind(self):
        """制冷"""
        pass

    def hotWind(self):
        """制热"""
        pass

    def swingLeftAndRight(self):
        """摆动"""
        pass


class MediaAC(AC):
    def coolWind(self):
        """制冷"""
        print("美的空调制冷")

    def hotWind(self):
        """制热"""
        print("美的空调制热")

    def swingLeftAndRight(self):
        """摆动"""
        print("美的空调摆动")

    def makeCool(ac: AC):
        # 运行
        ac.coolWind()


class GreeAC(AC):
    def coolWind(self):
        """制冷"""
        print("格力空调制冷")

    def hotWind(self):
        """制热"""
        print("格力空调制热")

    def swingLeftAndRight(self):
        """摆动"""
        print("格力空调摆动")

    def makeCool(ac: AC):
        # 运行
        ac.coolWind()
