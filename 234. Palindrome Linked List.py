# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.isPalindromeArray(arr)

    def isPalindromeArray(self, arr):
        left, right = 0, len(arr)-1
        while left < right:
            if arr[left] == arr[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

# Approach 2: not using array to store value, but reverse the second half of the linked list, and compare the value


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # find the middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        # start from the node slow (middle node)
        prev = None
        while slow:
            nex = slow.next
            slow.next = prev

            prev = slow
            slow = nex

        # compare, prev is the head of the second half
        while prev:
            if prev.val == head.val:
                prev = prev.next
                head = head.next
            else:
                return False

        return True
