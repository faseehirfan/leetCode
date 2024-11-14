# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. 

# TWO SOLUTIONS

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# LINEAR TIME, LINEAR SPACE SOLUTION
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToNew = { None: None}
        cur = head

        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            new = oldToNew[cur]
            new.next = oldToNew[cur.next]
            new.random = oldToNew[cur.random]
            cur = cur.next
        
        return oldToNew[head]

# LINEAR TIME, CONSTANT SPACE SOLUTION


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None

        cur = head
        while cur:
            new = Node(cur.val, cur.next)
            cur.next = new
            cur = new.next
        
        cur = head
        while cur:
            if cur.random: 
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        oldHead = head
        newHead = head.next
        curOld = oldHead
        curNew = newHead

        while curOld:
            curOld.next = curOld.next.next
            curNew.next = curNew.next.next if curNew.next else None
            curOld = curOld.next
            curNew = curNew.next

        return newHead
    
# EXPLANATION FOR SOLUTION 2: 

# Initialization and Interweaving:

# Traverse the original list.
# For each node, create a corresponding new node and place it between the current node and the current node's next.
# Setting Random Pointers:

# Traverse the interweaved list.
# For each old node, set its corresponding new node's random pointer.
# Separating Lists:

# Traverse the interweaved list again to separate the old and new lists.