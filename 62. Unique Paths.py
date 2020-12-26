class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*m for _ in range(n)]
        for col in range(1,m):
            for row in range(1,n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
                
        return dp[n-1][m-1]

sol = Solution()
print(sol.uniquePaths(3,5))

# Approach 2: top down with memorization
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         mem = [[None] * m for _ in range(n)]
#         if m <= 0 or n <= 0: return 0
#         if m == 1 and n == 1: return 1
#         if mem[n-1][m-1]:
#             return mem[n-1][m-1]
#         else:
#             res = self.uniquePaths(m-1,n) + self.uniquePaths(m, n-1)
#             mem[n-1][m-1] = res
#             return res

# Approach 3: math (way of thinking using fatorial)
# This one is soooooooo cool!!
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2) // factorial(m-1)//factorial(n-1)      