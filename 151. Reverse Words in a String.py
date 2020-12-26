151. Reverse Words in a String
from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        # Approach 1: use the built-in functions
        # return " ".join(reversed(s.split()))
    
        # Approach 2: deque of words
        left, right = 0, len(s)-1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1
        
        d, words = deque(),[]
        # push word by word in front of deque
        while left <= right:
            if s[left] == ' ' and words:
                d.appendleft(''.join(words))
                words = []
            elif s[left] != ' ':
                words.append(s[left])
            left += 1
            
        d.appendleft(''.join(words))
        
        return ' '.join(d)

sol = Solution()
print(sol.reverseWords('  leetcode  is     fun'))