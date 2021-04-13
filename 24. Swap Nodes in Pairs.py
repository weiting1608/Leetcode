# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        fNode = head
        sNode = head.next

        fNode.next = self.swapPairs(sNode.next)
        sNode.next = fNode

        return sNode
