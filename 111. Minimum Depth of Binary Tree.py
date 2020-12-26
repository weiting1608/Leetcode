# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# different from maxDepth, more edge cases need to be considered.
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        # no child at all, 2nd not is important.
        if not root.left and not root.right: 
            return 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not root.left: 
            return 1+r
        if not root.right: 
            return 1+l
        return min(l,r) + 1