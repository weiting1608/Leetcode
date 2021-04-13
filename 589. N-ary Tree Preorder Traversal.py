"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Approach 1: recursive
# time complexity: O(n)
# space complexity: O(h) -- worst case O(n)
class Solution:
    def __init__(self):
        self.res = []
        
    def preorder(self, root: 'Node') -> List[int]:        
        if root:
            self.res.append(root.val)
            for child in root.children:
                self.preorder(child)
            
        return self.res

# Approach 2: iterative
# time complexity: O(n)
# space complexity: O(h) -- worst case O(n)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:        
        if not root: return []
        
        stack, res = [root], []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
            
        return res        
        
        