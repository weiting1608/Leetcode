# Approach 1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
                
        return "".join(prefix)

# Approach 2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        prefix = []
        strs.sort()
        for x, y in zip(strs[0], strs[-1]):
            if x == y: prefix.append(x)
            else: break
        
        return "".join(prefix)

# Approach 3
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