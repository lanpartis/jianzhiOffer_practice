# -*- coding:utf-8 -*-
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
'''
class Solution:
    def InversePairs(self, data):
        # write code here
        result,_ =mergesort(data)
        return result%1000000007

def mergesort(raw_list):
    if len(raw_list) <2:
        return 0,raw_list
    middle = int(len(raw_list)/2)
    rev1,head = mergesort(raw_list[:middle])
    rev2,tail = mergesort(raw_list[middle:])
    rev3,merged_list = merge(head,tail)
    return (rev1+rev2+rev3)%100000007,merged_list

def merge(head,tail):
    merged_list=[]
    accumulator=0
    counter=0
    l1ptr=0
    l2ptr=0
    leng1 = len(head)
    leng2 = len(tail)
    while l1ptr<leng1 and l2ptr<leng2:
        if head[l1ptr]<tail[l2ptr]:
            accumulator += counter
            counter = 0
            merged_list.append(head[l1ptr])
            l1ptr +=1
        else:
            counter += leng1 - l1ptr
            merged_list.append(tail[l2ptr])
            l2ptr +=1
    if l1ptr<leng1:
        accumulator+= (leng1-l1ptr)*leng2
        merged_list.extend(head[l1ptr:])
    else:
        merged_list.extend(tail[l2ptr:])
    return accumulator,merged_list
