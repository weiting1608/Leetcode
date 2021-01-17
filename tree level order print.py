import collections

class TreeNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(6)

class Solution():
    def levelOrderPrint(self, tree):
        nodes = collections.deque([tree])
        # for node in nodes:
        #     print(node.val)

        if not tree: return

        currentCount = 1
        nextCount = 0

        while len(nodes):
            currentNode = nodes.popleft()
            currentCount -= 1

            print(currentNode.val, end =' ')

            if currentNode.left:
                nodes.append(currentNode.left)
                nextCount += 1
            
            if currentNode.right:
                nodes.append(currentNode.right)
                nextCount += 1

            if currentCount == 0:
                print("\n")
                currentCount, nextCount = nextCount, currentCount


sol = Solution()
sol.levelOrderPrint(tree)