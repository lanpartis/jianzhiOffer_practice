# -*- coding:utf-8 -*-
'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        l = root.left
        root.left = self.Mirror(root.right)
        root.right = self.Mirror(l)
        return root
