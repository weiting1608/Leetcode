class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        ranks = [0] * n
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            if ranks[px] > ranks[py]: parent[py] = px
            else:
                parent[px] = py
                if ranks[px] == ranks[py]:
                    ranks[py] += 1
                    
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    union(i, j)
                    
        return len(set(find(i) for i in range(n)))
                   
                   
        