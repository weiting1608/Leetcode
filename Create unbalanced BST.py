class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None

def createBST(nums):
    root = None
    for num in nums:
        root = insert(root, num)
    return root

def insert(root, val):
    if not root: return TreeNode(val)
    if val <= root.val:
        root.left = insert(root.left, val)
    if val > root.val:
        root.right = insert(root.right, val)
    return root

def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

if __name__ == '__main__':
    root = createBST([5,4,3,1,7,6])
    inorder(root)
