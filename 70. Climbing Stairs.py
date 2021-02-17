class Solution:
    def climbStairs(self, n: int) -> int:
        # recursion using memoization
        mem = [0] * (n+1)
        if n <= 1: return 1  
    
        for i in range(2, n+1):
            if not mem[i]:
                res = self.climbStairs(i-1) + self.climbStairs(i-2)
                mem[i] = res
        
        return mem[n]
        