# -*- coding:utf-8 -*-
'''
求1-N之间所有整数中1出现的次数之和
'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        return countOne(str(n))
def countOne(n):
    if int(n) == 0:
        return 0
    if len(n) == 1:
        return 1
    res = count(n)
    return res + countOne(n[1:])

def count(n):
    h = int(n[0])
    tail = int(n[1:])
    l = len(n)
    if h ==1:
        oh = tail+1
    else:
        oh = 10**(l-1)
    ot = h*(l-1)*10**(l-2)
    return oh + ot
