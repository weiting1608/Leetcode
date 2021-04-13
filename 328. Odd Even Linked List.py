# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Similar to 86. Partition List, use four pointers to form two separate linked list
    """

    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = oddHead = ListNode(0)
        even = evenHead = ListNode(0)
        count = 0

        while head:
            count += 1
            if count % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next

            head = head.next

        even.next = None

        odd.next = evenHead.next

        return oddHead.next
