class Solution:
    def countAndSay(self, n: int) -> str:
        memo = [0 for _ in range(n+1)]
        memo[1] = "1"
        for i in range(2, n+1):
            memo[i] = self.say(memo[i-1])
        return memo[n]
    
    def say(self, s):
        i = j = 0
        res = ""
        while j <= len(s):
            if s[i] != s[j]:
                res += str(j-i) + s[i]
                i = j
            j += 1
        # res += str(j-i) + s[i]
        return res
        
sol = Solution()
print(sol.countAndSay(11))