# -*- coding:utf-8 -*-
'''
一个链表中包含环，请找出该链表的环的入口结点。
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead is None:
            return None
        #Meet in loop
        pf = pHead
        ps = pHead
        if pf.next is None:
            return None
        while pf.next is not None:
            print(pf.val,ps.val)
            pf = pf.next
            if pf.next is None:
                return None
            if ps is pf:
                break
            pf = pf.next
            ps = ps.next
        while pHead is not ps.next:
            pHead=pHead.next
            ps=ps.next
        return pHead
