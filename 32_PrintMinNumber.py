# -*- coding:utf-8 -*-
'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ""
        sort(numbers)
        res = ''
        for i in numbers:
            res+=str(i)
        return int(res)
def lt(a,b):
    a = str(a)
    b = str(b)
    res1 = int(a+b)
    res2 = int(b+a)
    return res1 >= res2
def sort(l,low=0,high='nd'):
    if high == 'nd':
        high = len(l)-1
    if low > high:
        return []
    if high == low:
        return l
    mid = partition(l,low,high)
    sort(l,low,mid-1)
    sort(l,mid+1,high)
def partition(l,low,high):
    key = l[low]
    while low<high:
        while low<high and (lt(l[high],key) or key == l[high]):
            high-=1

        if low<high:
            l[low] = l[high]
        while low<high and (lt(key,l[low])):
            low+=1

        if low<high:
            l[high] = l[low]
    l[low] = key
    return low
