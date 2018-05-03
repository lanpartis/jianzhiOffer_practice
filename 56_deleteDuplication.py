# -*- coding:utf-8 -*-
'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        head_ptr = ListNode(-1)
        head_ptr.next = pHead
        p = head_ptr
        while p.next is not None:
            has_dup=False
            while p.next.next is not None and p.next.next.val == p.next.val:
                p.next.next = p.next.next.next
                has_dup=True
            if has_dup:
                p.next = p.next.next
            else:
                p=p.next
        return head_ptr.next
