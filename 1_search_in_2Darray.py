#coding=utf-8
#在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        height = len(array)
        width = len(array[0])
        i,j=0,width-1
        while(i<height and j>=0):
            ele = array[i][j]
            if ele == target:
                return True
            if ele > target:
                j-=1
            else:
                i+=1
        return False
