# -*- coding:utf-8 -*-
'''
判断是否是平衡二叉树
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return isBalanced(pRoot)[1]
def isBalanced(pRoot):
    if pRoot == None:
            return 0,True
    lres = isBalanced(pRoot.left)
    rres = isBalanced(pRoot.right)
    if not (lres[1] and rres[1]):
        return -1,False
    if not (abs(lres[0]-rres[0])<=1):
        return -1,False
    return max(lres[0],rres[0])+1,True
