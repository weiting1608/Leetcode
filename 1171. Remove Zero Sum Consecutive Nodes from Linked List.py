# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head:
            return None

        curr = head
        temp = 0

        while curr:
            temp += curr.val
            curr = curr.next
            if temp == 0:
                return self.removeZeroSumSublists(curr)

        return ListNode(head.val, self.removeZeroSumSublists(head.next))
