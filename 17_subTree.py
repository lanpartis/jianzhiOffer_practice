# -*- coding:utf-8 -*-
'''

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        return DFS(pRoot1,pRoot2)

def DFS(root,root2):
    if root is None or root2 is None:
        return False
    if root.val == root2.val:
        if check(root,root2):
            return True
    node = DFS(root.left,root2)
    if node is False:
        node = DFS(root.right,root2)
    return node
def check(root,root2):
    if root is None or root2 is None:
        return False
    if root.val != root2.val:
        return False
    if root2.left is None:
        if root2.right is None:
            return True
        else:
            return check(root.right,root2.right)
    else:
        if root2.right is None:
            return check(root.left,root2.left)
    return check(root.left,root2.left) and check(root.right, root2.right)
