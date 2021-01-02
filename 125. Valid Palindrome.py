class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Useful typical way of clean up the string
        s = "".join([c for c in s if c.isalpha() or c.isnumeric()]).lower()
        
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]: return False
            
        else: return True
