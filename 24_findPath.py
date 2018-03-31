# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''
PATHS =[]
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        global PATHS
        PATHS = []
        if root is None:
            return PATHS
        path=[]
        s=0
        DFS(root,expectNumber,path,s)
        return PATHS
def DFS(root,number,path,s):
    path.append(root.val)
    if root.left is not None:
        DFS(root.left,number,path[:],s+root.val)
    if root.right is not None:
        DFS(root.right,number,path[:],s+root.val)
    if root.left is None and root.right is None:
        if root.val + s == number:
            PATHS.append(path)
