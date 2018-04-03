# -*- coding:utf-8 -*-
'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
字符串,长度不超过9(可能有字符重复),字符只包括大小写字母
'''
class Solution:
    def Permutation(self, ss):
        # write code here
        p = list(ss)
        p.sort()

        if len(p) is 0:
            return []
        l = len(p)
        indices = [0]
        for i in range(1,l):
            if p[i-1] != p[i]:
                indices.append(i)
        new_pers=[]
        for i in indices:
            newp = p[0:i]
            newp.extend(p[i+1:])
            pers = self.Permutation(newp)
            if len(pers)>=1:
                for per in pers:
                    n_per=p[i:i+1]
                    n_per.extend(per)
                    new_pers.append(n_per)
            else:
                n_per = p[i:]
                new_pers.append(n_per)
        for i in range(len(new_pers)):
            s = ''
            for j in new_pers[i]:
                s+=j
            new_pers[i] = s
        return new_pers
