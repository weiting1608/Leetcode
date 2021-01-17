# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        l1 = self.flipEquiv(root1.left, root2.left)
        l2 = self.flipEquiv(root1.left, root2.right)
        r1 = self.flipEquiv(root1.right, root2.right)
        r2 = self.flipEquiv(root1.right, root2.left)
        # 1st situation: same tree, 2nd situation: symmetric tree(flip之后仍相等)
        return root1.val == root2.val and ((l1 and r1) or (l2 and r2))
        