# -*- coding:utf-8 -*-
'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        return symme(pRoot.left,pRoot.right)
def symme(lroot,rroot):
    if lroot is None or rroot is None:
        if lroot == rroot:
            return True
        return False
    if lroot.val == rroot.val and symme(lroot.left,rroot.right) and symme(lroot.right,rroot.left):
        return True
    return False
