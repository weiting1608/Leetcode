19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # dummy is important to handle the edge case
        dummy = ListNode()
        dummy.next = head
        
        slow = fast = dummy
        # let fast goes n-1 steps ahead
        for _ in range(n):
            fast = fast.next
        
        # fast, slow goes simultaneously
        # slow will stop right before the (n-1)th node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # point the (n-1)th node to the (n+1)th node    
        slow.next = slow.next.next
        
        return dummy.next
        