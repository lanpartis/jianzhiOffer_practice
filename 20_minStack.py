# -*- coding:utf-8 -*-
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''
class Solution:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.minstack)==0:
            self.minstack.append(node)
            return
        m = self.minstack.pop()
        self.minstack.append(m)
        if node<m:
            self.minstack.append(node)
        else:
            self.minstack.append(m)

    def pop(self):
        self.minstack.pop()
        return self.stack.pop()
        # write code here
    def min(self):
        # write code here
        m = self.minstack.pop()
        self.minstack.append(m)
        return m
