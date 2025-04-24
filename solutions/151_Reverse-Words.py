class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        start = -1
        i = 0

        while i < len(s):
            if s[i] != " ":
                start = i
                while i < len(s) and s[i] != " ":
                    i += 1

                res.append(s[start:i])
                i -= 1
            i += 1

        return ' '.join(reversed(res))
    
    # 3 pass O(1) is to reverse the whole string and then reverse each word