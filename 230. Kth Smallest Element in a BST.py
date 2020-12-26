# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

 t1 = TreeNode(5)
 t2 = TreeNode(3)
 t3 = TreeNode(6)
 t4 = TreeNode(2)
 t5 = TreeNode(4)
 t6 = TreeNode(1)
 t1.left = t2
 t1.right = t3
 t2.left = t4
 t2.right = t5
 t4.left = t6

sol = Solution()
print(sol.kthSmallest(t1, 3))           
        # Approach 1: build inorder traversal tree and return the k-1 th element
#         def inorder(r):
#             if r:
#                 return inorder(r.left) + [r.val] + inorder(r.right)
#             else:
#                 return []
            
#         return inorder(root)[k-1]