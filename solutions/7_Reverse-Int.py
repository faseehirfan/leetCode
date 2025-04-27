class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        res = 0
        isNeg = x < 0
        while num > 0:
            res = res * 10 + num % 10
            num = num // 10

        if (-2)**31 > res or res > 2**31 - 1:
            return 0

        return -res if isNeg else res