class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        que = collections.deque([((0, 0), 0)])
        seen = {(0, 0)}

        while que:
            pos, step = que.popleft()
            if pos[0] == x and pos[1] == y:
                return step

            directions = [(1, 2), (2, 1), (2, -1), (1, -2),
                          (-2, 1), (-1, 2), (-2, -1), (-1, -2)]
            for d in directions:
                i, j = pos[0] + d[0], pos[1] + d[1]
                if (i, j) not in seen:
                    seen.add((i, j))
                    que.append(((i, j), step+1))
