class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in '+-*/':
                exp2 = stack.pop()
                exp1 = stack.pop()
                if t == '+':
                    stack.append(exp1 + exp2)
                elif t == '-':
                    stack.append(exp1 - exp2)
                elif t == '*':
                    stack.append(exp1 * exp2)
                else:
                    stack.append(int(exp1 / exp2))
            else:
                stack.append(int(t))
        return stack[-1]

