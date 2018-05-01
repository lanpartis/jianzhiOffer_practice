'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        i=0
        j=len(array)-1
        while(i<j):
            if array[i]+array[j]>tsum:
                j-=1
            elif array[i]+array[j]<tsum:
                i+=1
            else:
                return array[i],array[j]
        return []
