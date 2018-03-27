# -*- coding:utf-8 -*-
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        for i in range(len(array)):
            for j in range(len(array)-1,i,-1):
                if array[j]%2 ==1 and array[j-1]%2==0:
                    t = array[j-1]
                    array[j-1]=array[j]
                    array[j]=t
        return array
