# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        target = tail = head
        for _ in range(n): 
            tail = tail.next

        if not tail: return head.next

        while tail.next:
            target = target.next
            tail = tail.next

        target.next = target.next.next

        return head
