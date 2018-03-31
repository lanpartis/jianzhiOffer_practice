# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
'''
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        head = pHead
        while head is not None:
            new = RandomListNode(head.label)
            new.next = head.next
            head.next = new
            head = new.next
        nHead = pHead
        while pHead is not None:
            if pHead.random is not None:
                pHead.next.random = pHead.random.next
            pHead = pHead.next.next
        pHead = nHead
        nHead = nHead.next
        pHead.next = nHead.next
        pHead = pHead.next
        head = nHead
        while pHead is not None:
            nHead.next = pHead.next
            nHead = nHead.next
            pHead.next = nHead.next
            pHead = pHead.next

        return head
