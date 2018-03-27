# -*- coding:utf-8 -*-
#一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
ß
class Solution:
    def jumpFloor(self, number):
        # write code here
        f1 = 1
        f2 = 2
        if number==1:
            return f1
        elif number==2:
            return f2
        for i in range(2,number):
            f2 = f1 + f2
            f1 = f2 - f1
        return f2
