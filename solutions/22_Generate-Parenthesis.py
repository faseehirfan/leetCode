class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTrack(open, closed):
            if open == closed == n:
                res.append(''.join(stack))
                return

            if open < n:
                stack.append('(')
                backTrack(open+1, closed)
                stack.pop()

            if closed < open:
                stack.append(')')
                backTrack(open, closed+1)
                stack.pop()
            
        backTrack(0,0)
        return res

## OR USE A PATH VARIABLE INSTEAD OF A STACK
