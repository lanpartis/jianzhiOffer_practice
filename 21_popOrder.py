# -*- coding:utf-8 -*-
'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
'''
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack=[]
        popV.reverse()
        for i in pushV:
            stack.append(i)
            stack,popV = popStack(stack,popV)
        if len(stack) is 0:
            return True
        return False
def popStack(stack,pop):
    if len(stack) is 0:
        return stack,pop
    s = stack.pop()
    p = pop.pop()
    if s==p:
        return popStack(stack,pop)
    stack.append(s)
    pop.append(p)
    return stack,pop
