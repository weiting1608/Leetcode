# Approach 2: using stack (妙)
# time complexity: O(n), n is the string length
# space complexity: O(n), for the stack.
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack is a list of list ["character", count]
        stack = []
        for i in range(len(s)):
            # check if the last letter appended in stack is equal to current letter
            if stack and s[i] == stack[-1][0]:
                stack[-1][1] += 1
                # if count of the letter becomes k then pop the letter from stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i], 1])

        return "".join([s*cnt for s, cnt in stack])


# Approach 1: bruto force
# time complexity: O(n^2/k): n is the string length, we scan the string no more than n/k times.
# space complexity: O(1)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        if len(s) < k:
            return s

        start, end = 0, 1
        res = s
        while end < len(s):
            count = 1
            while s[start] == s[end]:
                count += 1
                end += 1
                if count == k:
                    newStr = s[:start]+s[end:]
                    res = self.removeDuplicates(newStr, k)
                    if end > len(res):
                        return res

            if s[start] != s[end]:
                start = end
                end += 1

        return res
