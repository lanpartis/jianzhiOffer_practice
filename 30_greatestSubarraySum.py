# -*- coding:utf-8 -*-
'''
计算连续子向量的最大和
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = array[1]
        m_indice = [0,0]
        su = 0
        i = 0
        j = 0
        while j<len(array):
            if i==j:
                su = array[i]
            else:
                su += array[j]

            if su > res:
                res = su
                m_indice=[i,j]
            j+=1
            if su < 0:
                i = j

        return res
