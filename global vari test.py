class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.isValid(s, low+1, high) or self.isValid(s, low, high-1)
        return True
    
    def isValid(self, s, start, end):
        if s[start] != s[end]: return False
        return True

sol = Solution()
print(sol.validPalindrome("eeccccbebaeeabebccceea"))   