"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# time complexity: O(n)
# space complexity: O(n)


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        self.res = []
        que = collections.deque([root])

        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                level.append(node.val)
                que.extend(node.children)
            self.res.append(level)

        return self.res
