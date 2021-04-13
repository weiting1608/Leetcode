# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        curr = head
        count = 0
        # initialize a set here only to improve the time efficiency
        Gset = set(G)

        while curr:
            # not curr.next is for the last item in the set
            if curr.val in Gset and (not curr.next or curr.next.val not in Gset):
                count += 1
            curr = curr.next

        return count
