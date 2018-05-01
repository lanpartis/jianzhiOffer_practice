# -*- coding:utf-8 -*-
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        a=s
        has_e=False
        has_point=False
        num=''
        for i in range(len(a)):
            if isnum(a[i]):
                num+=a[i]
            elif a[i]=='.':
                if has_e is False and has_point is False:
                    num+=a[i]
                    has_point = True
                else:
                    return False
            elif a[i]=='e' or a[i] =='E':
                inte=num
                num=''
                has_e=True
            elif a[i]=='-' or a[i]=='+':
                if num=='':
                    num=a[i]
                else:
                    return False
            else:
                return False
        if has_e and num=='':
            return False
        return True
def isnum(s):
    if s<='9' and s>='0':
        return True
    return False
