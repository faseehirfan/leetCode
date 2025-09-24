class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # PYTHONIC solution
        # index = haystack.find(needle)
        # return index

        for i in range(len(haystack) - len(needle) + 1):
            matched = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    matched = False
                    break

            if matched:
                return i

        return -1
