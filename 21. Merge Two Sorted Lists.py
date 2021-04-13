
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Approach1: recursion, time and space complexity: O(n+m)
        if not l1: return l2
        elif not l2: return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Approach2: like merge sort of array, time complexity O(n+m), space complexity O(1) 
        # needs space less because no recursion call needed to store the temp val.
        dummy = ListNode(0)
        # make sure for each iteration the dummy is unchanged to keep the result
        prev = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            # like k += 1, needs to update the position to add new following node.   
            prev = prev.next
            
        prev.next = l1 if l1 else l2
        return dummy.next
        
        
        