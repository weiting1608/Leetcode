class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        if len(s) == 1: return 0
        
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        
        for i, char in enumerate(s):
            if dic[char] == 1:
                return i
        
        return -1
            
        