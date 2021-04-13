# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        use two extra pointer to reform the linked list. Nice nice.

        """
        before = beforeHead = ListNode(0)
        after = afterHead = ListNode(0)

        while head:
            if head.val < x:
                before.next = head  # similar to append fun
                before = before.next  # increment the index

            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None  # otherwise a cyclic linked list will be formed.

        before.next = afterHead.next
        return beforeHead.next
