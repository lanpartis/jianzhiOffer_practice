# -*- coding:utf-8 -*-
'''
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
A and a are not the same.
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        table={}
        for i in range(ord('a'),ord('z')+1):
            table[chr(i)] = -1
        for i in range(ord('A'),ord('Z')+1):
            table[chr(i)] = -1
        for i in range(len(s)):
            if table[s[i]] == -1:
                table[s[i]] = i
            else:
                table[s[i]] = -2
        m = -1
        for i in range(ord('a'),ord('z')+1):
            if table[chr(i)]>=0:
                if m == -1:
                    m = table[chr(i)]
                elif table[chr(i)] < m:
                    m = table[chr(i)]
        for i in range(ord('A'),ord('Z')+1):
            if table[chr(i)]>=0:
                if m == -1:
                    m = table[chr(i)]
                elif table[chr(i)] < m:
                    m = table[chr(i)]
        return m
