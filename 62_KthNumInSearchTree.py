# -*- coding:utf-8 -*-
'''
给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None or k <1:
            return None
        self.k = k
        return self.in_order(pRoot)
    def in_order(self,pRoot):
        if self.k==0:
            return None
        if pRoot.left:
            res1 = self.in_order(pRoot.left)
            if res1 is not None:
                return res1
        if self.k == 1:
            return pRoot
        else:
            self.k-=1
        if pRoot.right:
            res2 = self.in_order(pRoot.right)
            if res2 is not None:
                return res2
        return None
