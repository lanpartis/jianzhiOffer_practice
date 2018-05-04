# -*- coding:utf-8 -*-
'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if len(matrix)==0 or rows == 0 or cols ==0:
            return False
        if len(path)==0:
            return True
        flag=[]
        mat=[]
        for i in range(rows):
            col = []
            flr = []
            for j in range(cols):
                col.append(matrix[i*cols+j])
                flr.append(0)
            mat.append(col)
            flag.append(flr)
        print(mat)
        for i in range(rows):
            for j in range(cols):
                if bt(mat,flag,i,j,path):
                    return True
        return False

def bt(mat,flag,row,col,s):
#     print(flag,row,col,s)
    if row>=len(mat) or row<0 or col>=len(mat[0]) or col<0 or flag[row][col] == 1 or mat[row][col] != s[0]:
        return False
    if len(s) == 1:
        return True
    n_flag=[]
    for i in flag:
        n_flag.append(i[:])
    flag=n_flag
    flag[row][col] = 1
    return bt(mat,flag,row+1,col,s[1:]) or bt(mat,flag,row-1,col,s[1:]) or bt(mat,flag,row,col+1,s[1:]) or bt(mat,flag,row,col-1,s[1:])
