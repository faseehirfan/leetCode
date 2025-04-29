class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_el = max(nums)
        res = 0
        l = 0
        seen = 0

        for r in range(len(nums)):
            if nums[r] == max_el:
                seen += 1

            while seen > k or (l <= r and seen == k and nums[l] != max_el):
                if nums[l] == max_el:
                    seen -= 1
                l += 1

            if seen == k:
                res += l + 1

        return res
                
            

