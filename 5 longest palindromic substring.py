class Solution:
    def longestPalindrome(self, s: str) -> str:
#         # Time limited exceed, bad Approach
#         # Time complexity : O(n^3)
#         substrings = []
#         for i in range (len(s)):
#             for j in range(i,len(s)):
#                 substrings.append(s[i:j+1])
                
#         long_palin = ""
#         for strp in substrings:
#             if strp == strp[::-1] and len(strp) > len(long_palin):
#                 long_palin = strp
                
#         return long_palin
        


# sol = Solution()
# print(sol.longestPalindrome("a"))
        # Approach 2: Expand Around Center
        if s == None or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i) # for odd palindrome
            len2 = self.expandAroundCenter(s, i, i+1) # for even palindrome
            leng = max(len1, len2)
            
            if leng > (end - start):
                start = i - (leng - 1) // 2
                end = i + leng // 2
                
        return s[start:end+1]
    
    def expandAroundCenter(self, s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right-left-1
                                    
sol = Solution()
print(sol.longestPalindrome("abccacbca"))

        