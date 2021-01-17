# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root: return
        # case 1: root and root左子树都不能要了
        if root.val < low: return self.trimBST(root.right, low, high)
        # case 2: root and root右子树都不能要了
        elif root.val > high: return self.trimBST(root.left, low, high)
        # case 3: root值合适，更新左子树和右子树
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        
        
        








