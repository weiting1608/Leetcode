# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        # close the linked list into the ring
        # while loop is for calculate the n
        pre_tail = head
        n = 1
        while pre_tail.next:
            pre_tail = pre_tail.next
            n += 1
        pre_tail.next = head
        
        # find new tail: (n-k%n-1)th node
        # find new head: (n-k%n)th node
        new_tail = head
        for i in range(n - k%n -1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head


sol = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
node = sol.rotateRight(l1,2)
while node is not None:
    print(node.val, end = "-")
    node = node.next
