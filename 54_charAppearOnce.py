'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''
class Solution:
    # 返回对应char
    def __init__(self):
        self.count = [0 for i in range(256)]
        self.out_que = []
    def FirstAppearingOnce(self):
        for i in self.out_que:
            if self.count[ord(i)]==1:
                return i
        return '#'
    def Insert(self, char):
        self.count[ord(char)]+=1
        self.out_que.append(char)
