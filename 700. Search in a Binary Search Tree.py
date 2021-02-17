# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
看到example 给的output是个array的时候，以为要返回一个数组，其实只要返回找到的根节点就好了
"""

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Approach 1: recursion
        if not root: return None
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return root
        
        return None

        # Approach 2: bfs 
        # 并没有用到binary search tree的特性
        bfs = [root]
        while bfs:
            # node 相当于recursion, 若bfs里是node.left, 则相当于 node = node.left
            node = bfs.pop(0)
            if node.val == val:
                return node
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return None
            
        
        