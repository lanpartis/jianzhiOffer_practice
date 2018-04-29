# -*- coding:utf-8 -*-
'''
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        S = tsum
        if S%2 ==0:
            end = S/2
        else:
            end = int(S/2) +1
        phead=1
        ptail=1
        result = []
        while(phead<end):
            su=sum(range(phead,ptail+1))
            if su>S:
                phead+=1
            if su<S:
                if ptail>= end:
                    break
                ptail+=1
            if su == S:
                result.append(list(range(phead,ptail+1)))
                phead += 2
                ptail += 1

        return result
