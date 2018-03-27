# -*- coding:utf-8 -*-
#给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
class Solution:
    def Power(self, base, exponent):
        # write code here
        res = 1
        if exponent >0:
            for i in range(exponent):
                res*=base
        elif exponent<0:
            for i in range(abs(exponent)):
                res*=base
            res = 1/res
        else:
            if base ==0:
                return 0
            else:
                return 1
        return res
