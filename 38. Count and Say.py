class Solution:
    def countAndSay(self, n: int) -> str:
        # initializa an array with n zero.
        memo = [0 for _ in range(n+1)]
        memo[1] = "1"
        for i in range(2, n+1):
            memo[i] = self.say(memo[i-1])
        return memo[n]
    
    def say(self, s):
        i, j = 0, 1
        res = ""
        while j < len(s):
            # when not equal, means the equal number has been traversed, need to summary count and value.
            if s[i] != s[j]:
                res += str(j-i) + s[i]
                i = j
            j += 1
        # last group, no need to compare, just attach j-i times of s[i]
        res += str(j-i) + s[i]
        return res
        