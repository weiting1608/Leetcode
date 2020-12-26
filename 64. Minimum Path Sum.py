class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        for col in range(m):
            for row in range(n):
                if col == 0 and row == 0:
                    before = 0
                elif col == 0:
                    before = grid[col][row-1]
                elif row == 0:
                    before = grid[col-1][row]
                else:
                    before = min(grid[col-1][row], grid[col][row-1])
                grid[col][row] = before + grid[col][row]
        
        return grid[m-1][n-1]

