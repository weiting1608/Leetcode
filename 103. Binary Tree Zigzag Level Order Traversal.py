# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time complexity: O(n). we traverse the tree nodes once and only once.
                       # Deque for insertion and pop only take O(1) time, not array
# space complextiy: O(n). Acutally the level which contains the most leaf nodes.
                       # In a binary tree case, the maximum number of nodes that might 
                       # reside on the same L roughly equals to n/2. So O(n/2). 
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        que = collections.deque([root])
        res = []

        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                if node:
                    level.append(node.val)
                    que.extend([node.left, node.right])
            if level:
                res.append(level)
            
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = reversed(res[i])
        return res
                
        