class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for p in s:
            if p in parens and len(stack):
                if stack[-1] == parens[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return len(stack) == 0
                


