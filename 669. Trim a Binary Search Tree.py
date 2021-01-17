# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

tree2 = TreeNode(2)
tree3 = TreeNode(3)
tree1 = TreeNode(1, tree2, tree3)

nodes = collections.deque([tree1])
if tree1.left:
    print(tree1.left.val)
if tree1.right:
    print(tree1.right.val)

print(tree1.val)








