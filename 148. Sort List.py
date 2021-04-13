# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        res.sort()
        dummy = ListNode()
        curr = dummy
        for i in range(len(res)):
            newNode = ListNode(res[i])
            curr.next = newNode
            curr = curr.next

        return dummy.next
