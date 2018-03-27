# -*- coding:utf-8 -*-
'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        nList = ListNode(0)
        p = nList
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val >= pHead2.val:
                p.next = ListNode(pHead2.val)
                pHead2 = pHead2.next
            else:
                p.next = ListNode(pHead1.val)
                pHead1 = pHead1.next
            p = p.next
        if pHead1 is None:
            p.next = pHead2
        else:
            p.next = pHead1
        return nList.next
