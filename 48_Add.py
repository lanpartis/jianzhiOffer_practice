# -*- coding:utf-8 -*-
'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''
class Solution:
    def Add(self, num1, num2):
        # write code here
        a,s = num1,num2
        while(s!=0):
            a,s=(a^s)&0xFFFFFFFF,(a&s)<<1
        if a>>31 ==1:
            a-=1<<32
        return a
