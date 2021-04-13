"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# recursive
class Solution:
    def __init__(self):
        self.res = []
        
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            for child in root.children:
                self.postorder(child)
            self.res.append(root.val)
            
        return self.res

# iterative
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        
        stack, res = [root], []
        
        while stack:
            node = stack.pop()
            stack.extend(node.children)
            res.append(node.val)
            
        return res[::-1]
            