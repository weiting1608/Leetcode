import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = collections.Counter(t)
        # count is to keep track that how many chara in t has been found in s.
        # res is the length of the substring and the start position of the substring
        count, start, end, res = len(t), 0, 0, [float('inf'), 0]
        # outer loop for finding the string which satisfy the restriction
        while end < len(s):
            c[s[end]] -= 1
            if c[s[end]] >= 0:
                count -= 1
            end += 1
            
            while count == 0:
                # update the minimum window
                if end - start < res[0]:
                    res = (end-start, start)

                # substract the left pointer to check if the restriction is still satisfied. "count == 0"   
                c[s[start]] += 1
                if c[s[start]] > 0:
                    count += 1
                start += 1
                
        return s[res[1]:res[0]+res[1]] if res[0] != float('inf') else ''

        # more quicker version and easy to understand
        # https://www.youtube.com/watch?v=jSto0O4AJbM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {}, {}
        
        for c in t:
            countT[c] = countT.get(c,0)+1
    
        have, need = 0, len(countT)
        # res stores the left, right boundary
        res, resLen = [-1, -1], float('inf')
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0)+1
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update the result
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                # pop from the left of our window   
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
                    

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s,t))