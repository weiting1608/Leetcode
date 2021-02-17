# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # global variable
        self.res = 0
        # this is for calculating the height of the root tree, height: maximum length of left path/right path.
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            # stores the diameter, relationship between the height of left child and right child is left+right+2
            self.res = max(self.res, left+right+2)
            # height of the root tree
            return 1+max(left, right)
        
        dfs(root) # to get the self.res
        return self.res

        
        
        
        