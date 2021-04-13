# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
# time complexity: O(n)
# space complexity: O(h) -- worst case O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return 
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left, root.right = right, left
        
        return root
        