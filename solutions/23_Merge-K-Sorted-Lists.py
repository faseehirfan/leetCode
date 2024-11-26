# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Priority Queue approach
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        d = ListNode()                                                 
        tail = d
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            node = node.next
            if node: 
                heapq.heappush(heap, (node.val, i, node))

        return d.next

# Merge sort approach, divide and conquer
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                # len(mergedLists) == len(lists) // 2
                mergedLists.append(self.mergeLists(l1, l2))

            lists = mergedLists

        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 or l2
        return dummy.next