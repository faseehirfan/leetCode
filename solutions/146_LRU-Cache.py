# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# SOLUTION:

class Node(object):
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev, self.next = prev, next
    
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """ 
        self.capacity = capacity
        self.cache = {}
        self.left = self.right = Node(-1, -1) # left is LRU, right is MRU
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node): # remove from anywhere
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node): # add to the right, before the right sentinel
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next   

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
            
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.cache.pop(lru.key) # del self.cache[self.left.next.key]
            self.remove(lru)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# TAKEAWAYS:
# need to make your own node class and implement doubly linked list. i used a deque and got screwed. 