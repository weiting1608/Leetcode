class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if len(haystack) == 0 or len(haystack) < len(needle): return -1
            
        for h in range(len(haystack)-len(needle)+1):
            for n in range(len(needle)):
                if haystack[h+n] != needle[n]: break
            else: return h
        
        return -1
                
        
   
sol = Solution()
print(sol.strStr("hello","ll"))