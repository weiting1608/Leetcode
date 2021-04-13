# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            var1 = l1.val if l1 else 0
            var2 = l2.val if l2 else 0

            sumTemp = var1 + var2 + carry
            carry = sumTemp // 10
            res = sumTemp % 10

            newNode = ListNode(res)
            curr.next = newNode
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
