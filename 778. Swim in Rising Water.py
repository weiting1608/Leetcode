# Approach: heap (priority queue) 基本上是套用的BFS模板
"""
we always walk in the smallest one that is 4-directionally adjacent to ones we've visited.
when we reach the target, the largest number we've visited so far is the answer
"""
# time complexity: O(n^2logn). we may expand O(n^2) nodes in the grid, each one
#  requires O(logn) time to perform the heap operations.
# space complexity: O(n^2), the maximum size of the heap.

import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen, pq = {(0, 0)}, [(grid[0][0], 0, 0)]
        res = 0
        while pq:
            T, i, j = heapq.heappop(pq)
            res = max(res, T)
            if i == j == n-1:
                return res

            # neighbors explore
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if x < 0 or x >= n or y < 0 or y >= n or (x, y) in seen:
                    continue
                seen.add((x, y))
                heapq.heappush(pq, (grid[x][y], x, y))

        return res
