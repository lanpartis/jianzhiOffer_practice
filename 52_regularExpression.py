'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s is None or pattern is None:
            return False
        return one_word_match(s,pattern)
def one_word_match(s,pattern,s_ptr=0,p_ptr=0):
    if s_ptr > len(s):
        return False
    if p_ptr==len(pattern):
        if s_ptr==len(s):
            return True
        return False
    if p_ptr == len(pattern)-1 or pattern[p_ptr+1] != '*':
        if s_ptr<len(s) and (s[s_ptr] == pattern[p_ptr] or pattern[p_ptr] == '.'):
            return one_word_match(s,pattern,s_ptr+1,p_ptr+1)
        else:
            return False
    else:
        if s_ptr<len(s) and (s[s_ptr] == pattern[p_ptr] or pattern[p_ptr]=='.'):
            return one_word_match(s,pattern,s_ptr+1,p_ptr) or one_word_match(s,pattern,s_ptr+1,p_ptr+2) or one_word_match(s,pattern,s_ptr,p_ptr+2)
        else:
            return one_word_match(s,pattern,s_ptr,p_ptr+2)
