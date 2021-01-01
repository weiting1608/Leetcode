# important for string searching, used to show search results(database or browser)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if len(haystack) == 0 or len(haystack) < len(needle): return -1
        # native pattern search algorithm: worst case O(m(n-m+1)) (m is the len(needle), n is the len(haystack))
        for h in range(len(haystack)-len(needle)+1):
            for n in range(len(needle)):
                if haystack[h+n] != needle[n]: break
            else: return h
        
        return -1