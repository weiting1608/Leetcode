# important for string searching, used to show search results(database or browser)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if len(haystack) == 0 or len(haystack) < len(needle): return -1
        # Approach 1: native pattern search algorithm 
        # worst case O(m(n-m+1)) (m is the len(needle), n is the len(haystack))
        for h in range(len(haystack)-len(needle)+1):
            for n in range(len(needle)):
                if haystack[h+n] != needle[n]: break
            # here the else the quite important, without else, the return h will be executed with h=0 & n=0
            # here the else makes that when all haystack[h+n] == needle[n], this will be executed only.
            else: return h
        
        return -1

        # Approach 2: KMP
class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        
        if n == 0: return 0
        if m == 0 or m < n: return -1
        
        res = []
        lps = [0] * n
        self.computeLPS(n, needle, lps)
        i, j = 0, 0
        while i < m and j < n:
            if haystack[i] == needle[j] and j == n-1:
                # For the case not only one match, res stores all the start positions of all matches.
                res.append(i-j)
                # Used for reset j after a match has been found.
                j = lps[j-1]
                # Since the problem only requires the first match, so here just return the first element.
                return res[0]
            
            elif haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0: j = lps[j-1]
                else: i += 1
        return -1

        
    def computeLPS(self, n, needle, lps):
        leng, i = 0, 1
        lps[0] = 0
        while i < n:
            if needle[leng] == needle[i]:
                lps[i] = leng + 1
                leng += 1
                i += 1
            elif leng == 0:
                lps[i] = 0
                i += 1
            else:
                leng = lps[leng-1]
                
            
        
   
        
        

        

                
        
   
        
        

        

        