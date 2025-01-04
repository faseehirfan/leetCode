class Solution:
    def romanToInt(self, s: str) -> int:
        syms = {'M': 1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I': 1}
        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and syms[s[i]] < syms[s[i+1]]:
                res -= syms[s[i]]
            else: res += syms[s[i]]
        
        return res