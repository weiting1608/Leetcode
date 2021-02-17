# Can use counter package to save the get function
# import collections
# c = collections.Counter(s)

"""
the smallest in lexicographical order means for all the possibilities, you need to keep the one smallest.
For example, for "adbcb", you can have "adbc" and "adcb", whether to delete the 1st duplicate b or 2nd.
"adbc" has smallest in lexicographical, so the result is "adbc"
It is not sorting the characters, the result won't be "abcd".
"Stack" is used for the solution.
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = {}
        for cha in s:
            c[cha] = c.get(cha,0) + 1
        stack = []
        for i in s:
            c[i] -= 1
            if i in stack:
                continue
            while stack and stack[-1] > i and c[stack[-1]]:
                stack.pop()
            stack.append(i)
        
        return ''.join(stack)

sol = Solution()
print(sol.removeDuplicateLetters("cbacdcbc"))