class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        is_neg = False
        res = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        for i,c in enumerate(s):
            if i == 0 and c in '+-':
                is_neg = (c == '-')
                continue
            if c.isdigit():
                res = res*10 + int(c)
                if not is_neg and res >= INT_MAX:
                    return INT_MAX
                if is_neg and res >= -INT_MIN:  # abs value compare
                    return INT_MIN
            else:
                break

        return -res if is_neg else res
