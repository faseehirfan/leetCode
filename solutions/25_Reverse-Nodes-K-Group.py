# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse the group
            prev, cur = groupNext, groupPrev.next 
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur