# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        self.nodes = []
        head = pointer = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next

        for x in sorted(self.nodes):
            pointer.next = ListNode(x)
            pointer = pointer.next
        return head.next

sol = Solution()
print(sol.mergeKLists([1,4,5],[1,3,4],[2,6]))