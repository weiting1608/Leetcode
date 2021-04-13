class Solution:
    """
    we can think of this problem as a shortest path problem on a graph: 
    there are 10000 nodes(string '0000' to '9999'), and there is an edge between two nodes
    if they differ in one digit, that digit differs by 1 (wrapping around), and if both 
    nodes are not in deadends.
    """

    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        # template, neighbors are important
        # if there is no neighbor access, write your own.
        def neighbors(pw):
            for i in range(4):  # 4 digits in total
                old = int(pw[i])
                for d in (-1, 1):
                    new = (old+d) % 10  # %10 is for wrapping around condition
                    yield pw[:i]+str(new)+pw[i+1:]

        dead = set(deadends)
        que = collections.deque()
        seen = set()
        seen.add('0000')
        que.append(('0000', 0))

        while que:
            pw, step = que.popleft()
            if pw == target:
                return step
            elif pw in dead:
                continue
            for nei in neighbors(pw):
                if nei not in seen:
                    seen.add(nei)
                    que.append((nei, step+1))

        return -1
