206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Approach 1: iterative
        # time complexity: O(n)
        # space complexity: O(1)
        current = head
        previous = None

        while current:
            nextnode_temp = current.next  # save the next
            current.next = previous  # reverse

            previous = current   # update curr & prev
            current = nextnode_temp

        return previous  # new head at end

        # Approach 2: recursive
        # time complexity: O(n)
        # space complexity: O(n) because you need a stack to store the current head

        if not head or not head.next:
            return head

        p = self.reverseList(head.next)  # down down down
        head.next.next = head  # add me
        head.next = None
        return p  # return upwards
