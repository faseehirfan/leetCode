class Solution:
    def minOperations(self, s: str) -> int:
        zerofirst = 0
        onefirst = 0
        
        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == '0':
                    onefirst += 1
                else:
                    zerofirst += 1
            else:
                if c == '1':
                    onefirst += 1
                else:
                    zerofirst += 1
        return min(zerofirst, onefirst)
