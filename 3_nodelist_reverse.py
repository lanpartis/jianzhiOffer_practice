# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
s=[]
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        global s
        s = []
        if listNode != None:
            addnode(listNode)
        return s

def addnode(node):
    if node.next:
        addnode(node.next)
    s.append(node.val)
