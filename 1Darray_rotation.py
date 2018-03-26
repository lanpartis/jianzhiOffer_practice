# -*- coding:utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        tail = len(rotateArray)
        if tail == 0:
            return 0
        head = 0
        tail -= 1
        mid = int((tail+head)/2)
        while(tail!= head+1):
            if rotateArray[mid]>rotateArray[head]:
                head = mid
                mid = int((tail+head)/2)
            elif rotateArray[mid]<rotateArray[head]:
                tail = mid
                mid = int((tail+head)/2)
            elif rotateArray[mid] == rotateArray[head]:
                if rotateArray[mid] >rotateArray[tail]:
                    head = mid
                    mid = int((tail+head)/2)
                else:
                    prev = rotateArray[head]
                    for i in range(head+1,tail):
                        if rotateArray[i]<prev:
                            return rotateArray[i]
                        prev = rotateArray[i]
        return rotateArray[tail]
