class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = r = res = 0

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res

# Optimized version
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res