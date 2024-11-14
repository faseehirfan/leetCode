# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            res[tuple(sorted(s))].append(s)
        
        return res.values()


# above solution is O(mnlogn) which is fine since we know word length will be less than 100, if word length was massive, (log(n) > 26)
# then belows solution is more optimal with a O(mn) complexity. 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()