# -*- coding:utf-8 -*-
'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        if pRootOfTree.left is not None:
            pRootOfTree.left=self.Conv(pRootOfTree.left,True)
            pRootOfTree.left.right = pRootOfTree
        if pRootOfTree.right is not None:
            pRootOfTree.right=self.Conv(pRootOfTree.right,False)
            pRootOfTree.right.left = pRootOfTree
        while pRootOfTree.left is not None:
                pRootOfTree = pRootOfTree.left
        return pRootOfTree
    def Conv(self,pRootOfTree,left):
        if pRootOfTree.left is not None:
            pRootOfTree.left=self.Conv(pRootOfTree.left,True)
            pRootOfTree.left.right = pRootOfTree
        if pRootOfTree.right is not None:
            pRootOfTree.right=self.Conv(pRootOfTree.right,False)
            pRootOfTree.right.left = pRootOfTree
        if left:
            while pRootOfTree.right is not None:
                pRootOfTree = pRootOfTree.right
        else:
            while pRootOfTree.left is not None:
                pRootOfTree = pRootOfTree.left
        return pRootOfTree
