# -*- coding:utf-8 -*-
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        now = None
        counter = 0
        for i in numbers:
            if now == None:
                now = i
                counter = 1
                continue
            if i == now:
                counter+=1
            else:
                counter-=1
            if counter is 0:
                now=None
        if counter>0:
            check=0
            for i in numbers:
                if i == now:
                    check+=1
            if check>=(len(numbers))/2:
                return now
        return 0
