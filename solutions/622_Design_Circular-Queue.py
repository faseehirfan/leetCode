class MyCircularQueue:
    def __init__(self, k: int):
        self.count = 0
        self.size = k
        self.q = [-1] * k
        self.headIdx = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[(self.headIdx + self.count) % self.size] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.q[self.headIdx] = -1
        self.headIdx = (self.headIdx + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.headIdx]

    def Rear(self) -> int:
        return self.q[(self.headIdx + self.count - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()