# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k<1 or head is None:
            return None
        kth = head
        for i in range(k-1):
            if kth.next is None:
                return None
            kth = kth.next
        while kth.next is not None:
            kth = kth.next
            head = head.next
        return head
