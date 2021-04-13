# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach 1: using a set to store the node of one list,
# Time complexity O(m+n)
# Space complexity O(m) or O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next

        while headB:
            if headB in seen:
                return headB
            else:
                headB = headB.next

        return None

# Approach 2: basic idea is from the end of two linked lists.
# If there is an intersection, the last node must be the same.
# Then start the comparison from the length difference node.
# The below implementation is a bit tricky using math characteristic.
# you can also write more complex get the length first and then start from
# the some node in the longer list to optimize the space complexity to O(1).


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1

# more complex implementation with same time & space complexity with approach 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m, n = 0, 0
        pa, pb = headA, headB
        while pa:
            pa = pa.next
            m += 1

        while pb:
            pb = pb.next
            n += 1

        if m >= n:
            diff = m-n
            while diff:
                headA = headA.next
                diff -= 1
        else:
            diff = n-m
            while diff:
                headB = headB.next
                diff -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
