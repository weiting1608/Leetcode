# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def dfs(root):
            if not root:
                return
            
            dfs(root.right)
            root.val += self.sum
            self.sum = root.val
            dfs(root.left)
            
        dfs(root)
        return root

tn1 = TreeNode(4)
tn2 = TreeNode(1)
tn3 = TreeNode(6)
tn4 = TreeNode(2)
tn1.left = tn2
tn1.right = tn3
tn2.right = tn4
sol = Solution()
print(sol.bstToGst)