class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        window = Counter()
        have, need = 0, len(tcount)
        res , reslen = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window.update(c)

            if c in tcount and window[c] == tcount[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = [l,r]
                
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != float('inf') else ""