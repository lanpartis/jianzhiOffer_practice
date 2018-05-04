# -*- coding:utf-8 -*-
'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''
class Solution:
    def __init__(self):
        self.odd=False
        self.max_heap=[0]
        self.min_heap=[0]
    def Insert(self, num):
        # write code here
        if len(self.max_heap)==1:
            self.max_heap.append(num)
            self.odd = True
            return
        if len(self.min_heap)==1:
            if num < self.max_heap[1]:
                t=num
                num=self.max_heap[1]
                self.max_heap[1]=t
            self.min_heap.append(num)
            self.odd = False
            return
        if self.odd:
            if num<self.max_heap[1]:
                t = num
                num = self.max_heap[1]
                self.max_heap[1] = t
                heap_sort(self.max_heap,1,lgt)
            self.min_heap.append(num)
            heap_sort(self.min_heap,1,lst)
        else:
            if num>self.min_heap[1]:
                t = num
                num = self.min_heap[1]
                self.min_heap[1]=t
                heap_sort(self.min_heap,1,lst)
            self.max_heap.append(num)
            heap_sort(self.max_heap,1,lgt)
        self.odd = not self.odd
    def GetMedian(self,data):
        # write code here
        if self.odd:
            return self.max_heap[1]
        return (float(self.min_heap[1]+self.max_heap[1]))/2
lgt = lambda a,b:a>=b
lst = lambda a,b:a<b
def heap_sort(root,idx,func=lgt):
    if len(root)>idx*2+1:
        heap_sort(root,idx*2+1,func)
        if func(root[idx*2+1],root[idx]):
            t = root[idx]
            root[idx] = root[idx*2+1]
            root[idx*2+1] = t
    if len(root)>idx*2:
        heap_sort(root,idx*2,func)
        if func(root[idx*2],root[idx]):
            t = root[idx]
            root[idx] = root[idx*2]
            root[idx*2] = t
