'''
统计一个数字在排序数组中出现的次数。
'''
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0:
            return 0
        if k <data[0] or k>data[-1]:
            return 0
        head = binary_search_head(data,0,len(data),k)
        tail = binary_search_tail(data,0,len(data),k)
        if head is not None:
            return tail - head + 1
        return 0

def binary_search_head(li,head,tail,target):
    if head >tail:
        return None
    mid = int((head+tail)/2)
    print(mid)
    if li[mid] == target:
        if mid > 0:
            if li[mid-1] ==target:
                return binary_search_head(li,head,mid-1,target)
        return mid
    if li[mid]>target:
        return binary_search_head(li,head,mid-1,target)
    return binary_search_head(li,mid+1,tail,target)
def binary_search_tail(li,head,tail,target):
    if head >tail:
        return None
    mid = int((head+tail)/2)
    if li[mid] == target:
        if mid < len(li)-1:
            if li[mid+1] ==target:
                return binary_search_tail(li,mid+1,tail,target)
        return mid
    if li[mid]>target:
        return binary_search_tail(li,head,mid-1,target)
    return binary_search_tail(li,mid+1,tail,target)
