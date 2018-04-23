#coding=utf-8
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
class Solution:
    def __init__(self):
        #two stack A,B
        #list.append() is push and list.pop() is pop
        self.a=[]
        self.b=[]
    def push(self, node):
        # write code here
        self.a.append(node)
    def pop(self):
        # return xx
        if len(self.a) == 0:
            return None
        while len(self.a):
            self.b.append(self.a.pop())
        out = self.b.pop()
        while len(self.b):
            self.a.append(self.b.pop())
        return out
