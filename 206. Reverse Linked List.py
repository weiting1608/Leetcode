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
        previous, nextnode = None, None
        
        while current:
            nextnode_temp = current.next
            current.next = previous
            
            previous = current
            current = nextnode_temp
            
        return previous
        
        # Approach 2: recursive
        # time complexity: O(n)
        # space complexity: O(n) because you need a stack to store the current head
        
        if not head or not head.next:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    