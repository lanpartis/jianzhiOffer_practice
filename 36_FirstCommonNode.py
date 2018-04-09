# -*- coding:utf-8 -*-
'''

输入两个链表，找出它们的第一个公共结点。
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None:
            return None
        l1 = getLength(pHead1)
        l2 = getLength(pHead2)
        if l1 >= l2:
            for i in range(l1 - l2):
                pHead1=pHead1.next
        else:
            for i in range(l2 - l1):
                pHead2=pHead2.next
        while pHead1 is not None :
            if pHead1.val == pHead2.val:
                return pHead1
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next

def getLength(pHead):
    l = 0
    while pHead is not None:
        l+=1
        pHead = pHead.next
    return l
