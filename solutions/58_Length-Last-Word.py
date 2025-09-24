class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        started = False
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and not started:
                continue
            elif s[i] == " ":
                return res

            else:
                started = True
                res += 1

        return res
