# -*- coding:utf-8 -*-
'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
'''
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k==0:
            return []
        if len(tinput)<k:
            return []

        least_k(tinput,k,0,len(tinput)-1)
        res = tinput[:k]
        res.sort()
        return res

def least_k(tinput,k,low,high):
    if low>=high:
        return None
    res,index = partion(tinput,low,high)
#     print(res,index,k,low,high)
    if index+1 == k:
        return res[:index+1]

    if index+1 <k:
        return least_k(res,k-index+low,index+1,high)
    elif index+1 >=k:
        return least_k(res,k,low,index-1)

    return n_res

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return array,low
