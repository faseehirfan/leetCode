class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sind = tind = 0

        while sind < len(s) and tind < len(t):
            if s[sind] == t[tind]:
                sind += 1
            tind += 1

        return sind == len(s)
