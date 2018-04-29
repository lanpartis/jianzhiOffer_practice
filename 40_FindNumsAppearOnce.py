# -*- coding:utf-8 -*-
'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        res = xorarray(array)
        for i in range(len(bine(res))):
            if bine(res)[i] =='1':
                pos_of_1 = i
                break
        array_a = [i for i in array if bine(i)[pos_of_1] == '1']
        array_b = [i for i in array if bine(i)[pos_of_1] == '0']
        res_a = xorarray(array_a)
        res_b = xorarray(array_b)
        return [res_a,res_b]
def xorarray(array):
    res = array[0]
    for i in array[1:]:
        res^=i
    return res
def bine(i,ty=32):
    res = bin(i)
    res = res[2:]
    result=(ty-len(res))*'0'
    result+= res
    return result
