# -*- coding:utf-8 -*-
'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) is 0:
            return False
        if len(sequence) is 1 or len(sequence) is 2:
            return True
        center = sequence.pop()
        res,index = checkCenter(sequence,center)
        if res:
            if index is 0:
                return self.VerifySquenceOfBST(sequence[index:])
            if index is -1:
                return self.VerifySquenceOfBST(sequence)
            return self.VerifySquenceOfBST(sequence[:index]) and self.VerifySquenceOfBST(sequence[index:])
        return res
def checkCenter(seq,center):
    lst = True
    pos = -1
    for i in range(len(seq)):
        if lst:
            if seq[i]>center:
                lst = False
                pos = i
        else:
            if seq[i]<center:
                return False,-1
    return True,pos
