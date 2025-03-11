class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        freq = [0, 0, 0]
        res = l = r = found = 0

        while r < n:
            freq[ord(s[r]) - ord('a')] += 1
            if freq[ord(s[r]) - ord('a')] == 1:
                    found += 1

            while found == 3:
                res += n - r
                freq[ord(s[l]) - ord('a')] -= 1
                if freq[ord(s[l]) - ord('a')] == 0:
                    found -= 1
                l += 1

            r += 1

        return res
