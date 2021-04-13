# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        que = collections.deque([root])
        res = []
        
        while que:
            length = len(que)
            
            for i in range(length):
                node = que.popleft()
                
                if i == length-1:
                    res.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
        return res
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        que = collections.deque([root])
        res = []
        
        while que:
            length = len(que)
            
            for i in range(length):
                node = que.popleft()
                
                if i == length-1:
                    res.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
        return res
                
                