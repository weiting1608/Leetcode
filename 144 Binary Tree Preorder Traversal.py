# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach 1: recursive
    """
    Time complexity: O(N), where N is the number of nodes. We visit each node exactly once.
    Space complexity: up to O(H) to keep the recursion stack, where HH is a tree height.

    """
    def __init__(self):
        self.res = []
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root == None:
            return []
        
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        
        return self.res


# Approach 2: iterative
class Solution:
    def preorderTraversal(self,root):
        
        if root is None:
            return []

        stack, output = [root, ], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output