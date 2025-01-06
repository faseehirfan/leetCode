class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = 0
        seen = set()

        for x, c in count.items():
            if x not in seen and k-x in count:
                if x == k-x:
                    res += c//2
                else:
                    res += min(c, count[k-x])
                seen.add(x)
                seen.add(k-x)
        return res