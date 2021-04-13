# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approach 1: Do a inordertraver to get a sorted array
    def __init__(self):
        self.res = []
        
    def inorderTraverse(self, root):
        if root:
            self.inorderTraverse(root.left)
            self.res.append(root.val)
            self.inorderTraverse(root.right)
            
        return self.res
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = self.inorderTraverse(root)
        left, right = 0, len(arr)-1
        while left < right:
            if arr[left] + arr[right] == k:
                return True
            elif arr[left] + arr[right] > k:
                right -= 1
            else:
                left += 1
        return False
        
        # Approach 2: dfs + set
        def findTarget(self, root, k):
        s = set()
        def dfs(node):
            if node:
                if node.val in s:
                    return True
                s.add(k-node.val)
                return dfs(node.left) or dfs(node.right)
        return dfs(root)
            
        