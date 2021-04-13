
# Approach BFS and DFS(for using DFS, just change popleft() to pop())
# Time complexity: O(M * N)
# Space complexity: O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N).
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        # bfs is used for putting the node into visit set.
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    island += 1
                    bfs(r, c)

        return island
