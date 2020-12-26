# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        head: ListNode
         -> TreeNode
        """
        # base case
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        def findMid(head):
            slow = fast = head
            while fast and fast.next:
                prev = slow # prev here is introduced to chop the Linked List
                slow = slow.next
                fast = fast.next.next
            prev.next = None # necessary to cut the first part to another linked list
            return slow
        
        mid = findMid(head)
        root = TreeNode(mid.val)
        
        # LinkedList from head to mid-1, need to chop the LinkedList in findMid method
        root.left = self.sortedListToBST(head)
        # LinkedList from mid+1 to tail
        root.right = self.sortedListToBST(mid.next)
        
        return root