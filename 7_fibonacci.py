# -*- coding:utf-8 -*-
#输出斐波那契数列的第n项
class Solution:
    def Fibonacci(self, n):
        # write code here
        t0 = 0
        t1 = 1
        if n == 0:
            return t0
        for i in range(n-1):
            t1 = t0 + t1
            t0 = t1 - t0
        return t1
