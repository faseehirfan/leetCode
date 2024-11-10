class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:   
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0:
            # pop = x - oldself.min and self.min = x
            self.min = self.min - pop


    def top(self) -> int:
        top = self.stack[-1]
        if top < 0:
            return self.min
        return top + self.min

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()