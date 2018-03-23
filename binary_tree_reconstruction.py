# -*- coding:utf-8 -*-
'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        root = step(pre,tin)
        return root

def step(pre,tin):
    if len(pre) ==0:
        return
    subroot = TreeNode(pre[0])
    if len(pre) > 1:
        tinh,tint = splitTin(tin,pre[0])
        preh,pret = splitPre(pre,tinh)
        subroot.left = step(preh,tinh)
        subroot.right = step(pret,tint)
    return subroot

def splitTin(tin,root):
    tinh = []
    tint = []
    write = 1
    for i in tin:
        if i == root:
            write = 2
            continue
        if write==1:
            tinh.append(i)
        else:
            tint.append(i)
    return tinh,tint

def splitPre(pre,tinh):
    i = len(tinh)
    return pre[1:i+1],pre[i+1:]
