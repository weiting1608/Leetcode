# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time complexity: O(n). Because we traverse the entire input tree once. 
# space complexity: O(n) from O(h).
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left_subtree, right_subtree):
        if not left_subtree and not right_subtree: return True
        if not left_subtree or not right_subtree: return False
        l = self.isMirror(left_subtree.left, right_subtree.right)
        r = self.isMirror(left_subtree.right, right_subtree.left)
        return left_subtree.val == right_subtree.val and l and r
        