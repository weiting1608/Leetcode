# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dup = set()
        dummy = ListNode()
        dummy.next = head
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
                dup.add(curr.val)
            else:
                curr = curr.next

        curr2 = dummy
        while curr2.next:
            if curr2.next.val in dup:
                curr2.next = curr2.next.next
            else:
                curr2 = curr2.next
        return dummy.next


# Approach 2: use less space, no duplicate set is necessary.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        curr = head
        pre = dummy

        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                pre.next = curr.next
            else:
                pre = pre.next

            curr = curr.next

        return dummy.next
