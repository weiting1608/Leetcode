class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        
        # Approach 1: prefix sum: use extra space to store an affiliate array
        # It consider each candidate split, to consider how many 1s in the left partition, 
        # and how many 0s are in the right partition.
        # pre[i] is to store how many 1s existed before S[i], length is len(S) + 1
        # for each index j, 1s before j needs to be flipped, pre[j], 0s after j needs to be flipped too.
        # pre[len(S)]-pre[j] = # of 1s in the right partition, total number is len(S)-j, 
        # so # of 0s in the right partition is len(S)-j - (pre[len(S)-pre[j]]
        pre = [0]
        for b in S:
            pre.append(pre[-1]+int(b))
        
        ans = float('inf')
        for j in range(len(pre)):
            if pre[j] + len(S)-j-(pre[-1]-pre[j]) < ans:
                ans = pre[j] + len(S)-j-(pre[-1]-pre[j])
                
        return ans

        # Approach 2: dp: 2 dimension
        # col is for storing the case that this final string ended with 0 or 1.
        # pay attention to the range should be n+1.      
        n = len(S)
        dp = [[0] * 2 for i in range(n+1)]
        
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0] + (S[i-1] == '1')
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + (S[i-1] == '0')
            
        return min(dp[n][0], dp[n][1])
            