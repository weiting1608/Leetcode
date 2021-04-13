# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Approach 1: using set to store the visited node.
# Time complexity & space complexity O(n)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        visit = set()
        while head:
            if head in visit:
                return head
            else:
                visit.add(head)
                head = head.next

        return None

# Approach 2: two pointers
# To calcuate the meeting point where the slow and the fast point meet,
# assume c is the length of the cycle, a is the meeting point.
# 2d(slow) = d(fast) => 2(F+a) = (F+nc+a)
# F+a = nc => F = nc-a
# therefore, assign two pointers p1 and p2,
# p1 starts from head, p2 starts from a, then these two will meet at the entrance.


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        intersectNode = self.intersect(head)
        if not intersectNode:
            return None
        p1, p2 = head, intersectNode
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1

    def intersect(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None
