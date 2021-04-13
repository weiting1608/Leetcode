# DFS: coloring using 0, 1. Bit using is smart here.
# Time complexity: O(N+E), N is the number of nodes in the graphs, E is the number of edges.
#                  we explore each node once when we transform it from uncolored to colored, traversing all its edges
#                  in the neighbor process.
# Space complexity: O(N), the space used to store the color dict.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        stack = []
        for node in range(len(graph)):
            if node not in color:
                stack.append(node)
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        if color[nei] == color[node]:
                            return False

        return True
