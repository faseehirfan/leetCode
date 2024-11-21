class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        soFar = 0
        op = '+'
        s = s.replace(' ', '')

        for i, c in enumerate(s):
            if c.isdigit():
                soFar = soFar * 10 + int(c)
            
            if not c.isdigit() or i == len(s) - 1:
                if op == '+':
                    stack.append(soFar)
                elif op == '-':
                    stack.append(-soFar)
                elif op == '*':
                    stack.append(stack.pop() * soFar)
                elif op == '/':
                    stack.append(int(stack.pop() / soFar))
                
                op = c
                soFar = 0

        return sum(stack)