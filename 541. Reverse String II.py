541. Reverse String II
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        char = list(s)
        for i in range(0, len(s), 2*k):
            char[i:i+k] = reversed(char[i:i+k])
        return "".join(char)
        
# 这题刚开始一直在想怎么把s切割成每2k一个一个的字符串组成的list，忽略了
# range(0, len(s), 2*k)这个用法，想多了。此外，注意reversed func.