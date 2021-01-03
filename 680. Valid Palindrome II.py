# Approach 1: brute force, time complexity:O(n^2), space complexity: O(n) for the substring
# time exceeded for submission
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            sub = s[0:i]+s[i+1:len(s)]
            if self.validPalin(sub): return True
        return False
    
    def validPalin(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]: return False    
        return True
        
sol = Solution()
print(sol.validPalindrome("abca"))

# Approach 2: greedy algorithm
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointers, check s[low] == s[high], when there is no match, return delete the low-th or the high-th.
        # therefore, a valid palindrom with start and end func is necessary.
        low, high = 0, len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.isValid(s, low+1, high) or self.isValid(s, low, high-1)
        return True # first attempt: wrote return False here
    
    def isValid(self, s, start, end):
        while start < end:
            if s[start] != s[end]: return False
            else:
                start += 1
                end -= 1            
        return True

        