# -*- coding:utf-8 -*-
'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8=19。请问该机器人能够达到多少个格子？
'''
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        mat = [[0 for i in range(cols)] for j in range(rows)]
        dfs(mat,0,0,threshold,rows,cols)
        return sum(list(map(sum,mat)))
def dfs(mat,col,row,k,rows,cols):
    if col<0 or row<0 or row >= rows or col >= cols or mat[row][col]==1 or car_sum(col,row)>k:
        return False
    mat[row][col]=1
    dfs(mat,col+1,row,k,rows,cols)
    dfs(mat,col-1,row,k,rows,cols)
    dfs(mat,col,row+1,k,rows,cols)
    dfs(mat,col,row-1,k,rows,cols)
def car_sum(a,b):
    res=0
    while a is not 0:
        res +=a%10
        a=int(a/10)
    while b is not 0:
        res +=b%10
        b=int(b/10)
    return res
