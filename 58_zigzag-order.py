# -*- coding:utf-8 -*-
'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        out=[]
        n_line=[pRoot]
        reverse=False
        while True:
            n_out=[]
            line=n_line
            n_line=[]
            if line ==[]:
                return out
            for i in line:
                n_out.append(i.val)
                if i.left is not None:
                    n_line.append(i.left)
                if i.right is not None:
                    n_line.append(i.right)
            if reverse:
                n_out.reverse()
            out.append(n_out)
            reverse = not reverse
