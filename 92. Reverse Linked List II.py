# 92. Reverse Linked List II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # Function of dummy is to cover the case that m starts from head
        # Under this circumstance, pre still has the value (not out of range) 
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        
        # define the position of pre
        for _ in range(m-1):
            pre = pre.next
        
        curr = pre.next

        # change order
        for _ in range(n-m):
            extract = curr.next
            curr.next = extract.next
            extract.next = pre.next
            pre.next = extract
                        
        return dummy.next