# Approach: BFS
# time complexity: O(m*n). 1. We scan the grid to find the initial values O(m*n).
                      #  2. The BFS in the worst case would enumerate all cells once O(m*n).
                      #  In total, 2O(m*n) = O(m*n)
# space complexity: O(m*n). To store thr orange status.
"""
BTW, normall for BFS, the main space complexity lies in the process rather than the 
initialization. For instance, for a BFS traversal in a tree, at any given moment, the
queue would hold no more than 2 levels of tree nodes. Therefore, the space complexity 
of BFS traversal in a tree would depend on the width of the input tree.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        rotten = []
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    heapq.heappush(rotten, (0, grid[i][j], i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        while rotten:
            mins, orange, i, j = heapq.heappop(rotten)
            if not rotten and fresh == 0:
                return mins
            
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for d in directions:
                x, y = i+d[0], j+d[1]
                if x<0 or y<0 or x>=m or y>=n or grid[x][y] == 0:
                    continue
                elif grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh -= 1
                    heapq.heappush(rotten, (mins+1, grid[x][y], x, y))
                    
        return -1
                    
                    
            
        