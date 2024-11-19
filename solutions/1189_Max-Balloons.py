class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        tcount = Counter(text)
        bcount = Counter('balloon')
        res = len(text)

        for c in bcount:
            res = min(res, tcount[c] // bcount[c])
        return res
