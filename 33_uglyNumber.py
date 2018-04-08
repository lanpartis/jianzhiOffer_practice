# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        global last,ugly_list,length,i2,i3,i5
        last= 1
        ugly_list = [1,]
        length = 1
        i2 = 0
        i3 = 0
        i5 = 0
        if index==0:
            return 0
        if index==1:
            return 1
        last = 1
        for i in range(index-1):
            last = next_u(last)
        return last

def next_u(last):
    '''
    input last ugly number,
    output next ugly number .
    '''
    global i2,i3,i5,length
    for i in range(i2,length):
        candidate2 = ugly_list[i] * 2
        if candidate2 > last:
            candidate = candidate2
            candidatef = 2
            index = i
            break
    for i in range(i3,length):
        candidate3 = ugly_list[i] * 3
        if candidate3 > last:
            if candidate3 < candidate:
                candidate = candidate3
                candidatef = 3
                index = i
            break
    for i in range(i5,length):
        candidate5 = ugly_list[i] * 5
        if candidate5 > last:
            if candidate5 <candidate:
                candidate = candidate5
                candidatef =5
                index = i
            break
    ugly_list.append(candidate)
    length +=1
    if candidatef ==2:
        i2 = index
    elif candidatef ==3:
        i3 = index
    else:
        i5 = index
    return candidate
