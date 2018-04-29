# -*- coding:utf-8 -*-
'''
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
class Solution:
    def rectCover(self, number):
        # write code here
        if number==0:
            return 0
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
