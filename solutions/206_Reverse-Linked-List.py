# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recurse(prev, cur):
            if not cur: return prev
            nxt = cur.next
            cur.next = prev
            return recurse(cur, nxt)
        return recurse(None, head)
    
    # Iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev