# Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        alen = blen = 0
        start = headA
        while start:
            alen += 1
            start = start.next

        start = headB
        while start:
            blen += 1
            start = start.next
        
        diff = abs(alen - blen)
        start = headA if alen > blen else headB
        while diff:
            start = start.next
            diff -= 1
        
        start2 = headB if alen > blen else headA
        while start and start2:
            if start == start2:
                return start
            start = start.next
            start2 = start2.next
        
        return None