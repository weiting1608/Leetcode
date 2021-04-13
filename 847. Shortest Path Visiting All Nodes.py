# Approach 1: BFS + bit representation of visited nodes
# difficult to understand though faster. Goes for Approach 2.
# time complexity: O(2^n * n)
# space complexity: O(2^n * n)
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        que = collections.deque()
        # start point is uncertain, thus, all nodes are added.
        for i in range(n):
            que.append((1 << i, i))  # initialize the start point
            # que (nodeVisited, start), e.g., 0001, means only visited node 0
            # 0010, means only visited node 1, 'cause it shifts i-bit of 1 to the left.
            # 1111, end state, means all nodes have been visited.

        # default value 16 (largest value)
        dist = collections.defaultdict(lambda: n*n)
        for i in range(n):
            dist[1 << i, i] = 0  # self to self distance = 0

        goal = (1 << n) - 1  # left shift 1 n bit to get n-1 bits of '1'

        while que:
            nodeVisited, start = que.popleft()
            d = dist[nodeVisited, start]
            if nodeVisited == goal:
                return d
            for nei in graph[start]:
                newVisit = nodeVisited | (1 << nei)
                if d + 1 < dist[newVisit, nei]:
                    dist[newVisit, nei] = d + 1
                    que.append((newVisit, nei))


# Approach 2: just BFS
# time complexity: O(2^n * n)
# space complexity: O(2^n * n)
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        seen = set()
        que = collections.deque((i, [i]) for i in range(len(graph)))
        while len(que) > 0:
            n = len(que)
            for i in range(n):
                node, path = que.popleft()
                # shortest path must be the first which travelled all the nodes
                if len(set(path)) == len(graph):
                    # we can print the selected path here as well
                    return len(path)-1
                # explore paths with adjacent nodes
                for nei in graph[node]:
                    newPath = path + [nei]
                    key = self.getKey(graph, newPath, nei)
                    if key not in seen:
                        seen.add(key)  # only nei is not enough.
                        # because visiting the same node is necessary.
                        # e.g [[1,2,3],[0],[0],[0]], path is 1,0,2,0,3
                        # so we need this key to include non-visited nodes info.
                        que.append((nei, newPath))
        return 0

    # use (remaining nodes, current node) as key to avoid redundant traverse
    def getKey(self, graph, path, idx):
        arr = []
        m = set(path)
        for i in range(len(graph)):
            if i not in m:
                arr.append(i)
        return (tuple(arr), idx)
