# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle point, slow pointer
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev, curr = None, slow
        while curr:
            nex = curr.next
            curr.next = prev

            prev = curr
            curr = nex

        # merge two sorted linked list
        first, second = head, prev
        while second.next:
            tmp = first.next  # !!!!!! should store it first.
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp
        return head
