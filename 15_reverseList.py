# -*- coding:utf-8 -*-
'''
反转链表
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        h = pHead
        pre = None
        while h is not None:
            i = h.next
            h.next = pre
            pre = h
            h = i
        return pre
