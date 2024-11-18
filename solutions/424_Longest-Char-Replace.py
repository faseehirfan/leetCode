class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = maxf = l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            win_len = r - l + 1

            while win_len - maxf > k:
                count[s[l]] -= 1
                l += 1
                win_len -= 1
            
            res = max(res, win_len)
        return res