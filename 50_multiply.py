'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        F = [1]
        T = [1]
        for i in range(n-1):
            F.append(F[i]*A[i])
            T.append(T[i]*A[n-i-1])
        B=[]
        for i in range(n):
            B.append(F[i]*T[n-i-1])
        return B
