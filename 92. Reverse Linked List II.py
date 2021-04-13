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
            nex = curr.next

            curr.next = nex.next
            nex.next = pre.next
            pre.next = nex

        return dummy.next

# Approach 2: recursive approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m, n) -> ListNode:
        # m is the index of left position, n is the index of right position
        if not head:
            return
        left, right = head, head
        stop = False

        def reverseRecursion(right, m, n):
            # so that these two para won't be updated everytime function was called recursively.
            nonlocal left, stop

            # base case of recursion
            if n == 1:
                return
            # keep moving the right pointer one step forward until n == 1
            right = right.next

            # keep moving left pointer to until we reach the node to start the reverse
            if m > 1:
                left = left.next
            # recurse with m and n reduced
            reverseRecursion(right, m-1, n-1)

            # stop condition
            if left == right or right.next == left:
                stop = True

            # swap the value of the left and right node
            if not stop:
                left.val, right.val = right.val, left.val
                # move left pointer one step to the right
                # the right pointer moves one step back via backtracking,
                # 'cause the head used in the recursion func is right.
                left = left.next

        reverseRecursion(right, m, n)
        return head
