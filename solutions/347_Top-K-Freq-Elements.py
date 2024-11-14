# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        count = [[] for _ in range(len(nums) + 1)] 
        res = []

        for key, val in freq.items():
            count[val].append(key)

        for n in reversed(count):
            res.extend(n)
            if len(res) == k:
                return res
