# -*- coding:utf-8 -*-
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
'''
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        height = len(matrix)
        width = len(matrix[0])
        curser = [0,0]
        res = []
        while height>=2 and width>=2:
            for i in range(curser[1],curser[1]+width):
                res.append(matrix[curser[0]][i])
            for j in range(curser[0]+1,curser[0]+height):
                res.append(matrix[j][i])
            for k in range(curser[1]+width-2,curser[1]-1,-1):
                res.append(matrix[j][k])
            for l in range(curser[0]+height-2,curser[0],-1):
                res.append(matrix[l][k])
            curser[0]+=1
            curser[1]+=1
            height-=2
            width-=2
        if height is 0 or width is 0:
            return res
        if height is 1:
            for i in range(curser[1],curser[1]+width):
                res.append(matrix[curser[0]][i])
        elif width is 1:
            for l in range(curser[0],curser[0]+height):
                res.append(matrix[l][curser[1]])
        return res
