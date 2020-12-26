class Solution():
    def longestPalindrome(self, s):
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n-1): # avoid the first ^ and last $ symbol
            # ternary expression in python: [on_true] if [expression] else [on_false] 
            P[i] = min(R-i, P[2*C-i]) if R > i else 0                
            while(T[i+1+P[i]] == T[i-1-P[i]]):
                P[i] += 1

            if i + P[i] > R:
                C, R = i, i+P[i]
        
        maxLen, centerIndex = max((n,i) for i, n in enumerate(P))
        return s[(centerIndex - 1 - maxLen)//2: maxLen+1]

sol = Solution()
print(sol.longestPalindrome('babcbabcbaccba'))

        