# -*- coding:utf-8 -*-
'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
'''
class Solution:
    def __init__(self):
        self.sum=0
    def Sum_Solution(self, n):
        # write code here
        self.ite(n)
        return self.sum
    def ite(self,n):
        self.sum += n
        return n>0 and self.ite(n-1)
