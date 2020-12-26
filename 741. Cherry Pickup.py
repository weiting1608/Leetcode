# 以下是错的，记得回头看找错误，现在时间不太够刷hard
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        mem = [[[None]*N for _1 in range(N)] for _2 in range(N)]
        def dp(r1,c1,r2):
            c2 = r1+c1-r2
            if(r1<0 or c1<0 or r2<0 or c2<0) or (r1 == N or c1 == N or r2 == N or c2 == N) or (grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            elif r1 == c1 == N-1:
                return grid[r1][c1]
            elif mem[r1][c1][r2] is not None:
                return mem[r1][c1][r2]
            else:
                ans = grid[c1][r1] + (c1 != c2) * grid[c2][r2]
                ans += max(dp(r1+1,c1,r2), dp(r1,c1+1,r2), dp(r1+1,c1,r2+1), dp(r1,c1+1,r2+1))
            mem[r1][c1][r2] = ans
            return ans
        
        return max(0, dp(0,0,0))