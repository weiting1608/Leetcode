# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        count = 0
        ptr = head

        # first , see if there are at least k nodes left in the linked list
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        # when we have k node, then we need to reverse them
        if count == k:
            reversedHead = self.reverseLinkedList(head, k)
            # recurse on the remaining linked list
            # the recursion returns the head of the overall process list
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head

    def reverseLinkedList(self, head, k):
        # This function assumes that the list containes at least k nodes.
        prev, curr = None, head
        while k:
            # store the next node to process in the original list
            nex = curr.next

            # curr points to the previous node
            curr.next = prev
            # update the prev & curr
            prev = curr
            curr = nex

            k -= 1

        return prev
