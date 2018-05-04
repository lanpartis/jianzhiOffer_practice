# -*- coding:utf-8 -*-
'''
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res=[]
        if num==[] or size==0:
            return []
        if len(num) <size:
            return []
        max_que=[num[0]]
        TTL=[1]
        for i in range(1,size):
            add2que(max_que,TTL,num[i],i+1)
        res.append(max_que[0])
        #add number to queue
        for i in range(size,len(num)):
            for t in range(len(TTL)):
                TTL[t] -= 1
            if TTL[0]==0:
                TTL.remove(0)
                max_que.remove(max_que[0])
            add2que(max_que,TTL,num[i],size)
            res.append(max_que[0])
        return res
def add2que(max_que,TTL,num,life):
    for i in range(len(max_que)):
        tail = max_que.pop()
        if tail<num:
            TTL.pop()
        else:
            max_que.append(tail)
            max_que.append(num)
            TTL.append(life)
            return
    max_que.append(num)
    TTL.append(life)
    return
