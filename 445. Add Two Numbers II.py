# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        reverseL1 = self.reverseList(l1)
        reverseL2 = self.reverseList(l2)

        carry = 0
        dummy = ListNode()
        curr = dummy
        while reverseL1 or reverseL2 or carry:
            var1 = reverseL1.val if reverseL1 else 0
            var2 = reverseL2.val if reverseL2 else 0
            tempSum = var1 + var2 + carry
            carry = tempSum // 10
            res = tempSum % 10
            newNode = ListNode(res)
            curr.next = newNode
            curr = curr.next
            reverseL1 = reverseL1.next if reverseL1 else None
            reverseL2 = reverseL2.next if reverseL2 else None

        return self.reverseList(dummy.next)

    def reverseList(self, head):
        if not head:
            return
        curr = head
        prev = None
        while curr:
            nex = curr.next
            curr.next = prev

            prev = curr
            curr = nex

        return prev
