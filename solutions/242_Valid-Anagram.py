# Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)

        for char in t:
            if char in sCount:
                sCount[char] -= 1
                if sCount[char] == 0:
                    del sCount[char]
            else: return False
        return len(sCount) == 0

# Solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       return Counter(s) == Counter(t)