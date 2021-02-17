class Solution:
    def numDecodings(self, s: str) -> int:
        # edge case
        n = len(s)
        # empty or start with "0"
        if n == 0 or s[0] == "0": return 0
        if n == 1: return 1
        if n == 2:
            # start with > 2 followed by a non "0"
            if s[1] != "0": return 1 if int(s) > 26 else 2
            # followed by a "0"
            else: return 1 if int(s[0]) <= 2 else 0
            
        # for len(s) > 2
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if s[i] != "0":
                if 0 < int(s[i-1:i+1]) <= 26:
                    if s[i-1] != "0" and i == 1: 
                        dp[i] = 2
                    elif s[i-1] != "0" and i > 1:
                        dp[i] = dp[i-1] + dp[i-2] #### normal case, dp[i] = dp[i-1] + dp[i-2]
                    else:
                        dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1]
            else:
                # if s[i] == "0"
                if 0 < int(s[i-1:i+1]) <= 26:
                    if i == 1: dp[i] = 1
                    else: dp[i] = dp[i-2]
                        
        return dp[n-1]
            
sol = Solution()
print(sol.numDecodings("226"))        
        
        