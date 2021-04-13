"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Approach 1: BFS
# time complexity: O(n+m), n is number of nodes and m is number of edges.
# space complexity: O(n), space is used for seen dictionary and for the queue O(w) is 
# the width of the graph.
class Solution():
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        que = collections.deque([node])
        # dict to save the visited node to avoid cycles. 
        # {key: node of the original graph, value: corresponding cloned node of the graph}
        # therefore, for each original node, you need to instantiate a new Node object.
        seen = {}
        # clone the node and put it in the visited dictionary.
        seen[node] = Node(node.val, [])
        
        while que:
            n = que.popleft()
            # iterate through all the neighbors of the node
            for nei in n.neighbors:
                if nei not in seen:
                    # clone the neighbor and put it in visite if not existed
                    seen[nei] = Node(nei.val, [])
                    que.append(nei)
                # add the clone of the neighbor to the neighbors of the clone node "n"
                seen[n].neighbors.append(seen[nei])
            print("Node: "+str(seen[n].val))
            for no in seen[n].neighbors:
                print("Neighbors: "+str(no.val))
        # return the clone of the node from visited        
        return seen[node]
                
                
            
            
            
        