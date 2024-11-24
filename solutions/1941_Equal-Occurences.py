class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        maxVal = max(count.values())
        for val in count.values():
            if val != maxVal: return False
        return True