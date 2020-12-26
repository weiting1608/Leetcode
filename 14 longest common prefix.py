class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = ""
        for i in range(len(min(strs))):
            c = strs[0][i]
            # all: check if all elements in list/tuple/dic are true
            if all(a[i] == c  for a in strs):
                prefix += c
            else:
                break
                
        return prefix