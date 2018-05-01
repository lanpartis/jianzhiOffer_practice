# -*- coding:utf-8 -*-
'''
大\小 王可以看成任何数字
'''
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        s=numbers
        if len(s)!=5:
            return False
        numbers = [i for i in s if i != 0]
        joker = 5 - len(numbers)
        if max(numbers) - min(numbers)>4 or max(numbers) - min(numbers) + joker<4:
            return False
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if i == j :
                    return False
        return True
