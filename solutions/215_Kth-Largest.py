class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l,r):
            pivotIdx = random.randint(l,r)
            nums[pivotIdx], nums[r] = nums[r], nums[pivotIdx]
            pivot = nums[r]

            p = l
            lessEnd = -1
            for i in range(l, r):
                if nums[i] <= pivot:
                    if nums[i] < pivot:
                        lessEnd = p
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]

            if k > p:
                return quickSelect(p + 1, r)
            elif k > lessEnd:
                return nums[p]
            else:
                return quickSelect(l, lessEnd)

        return quickSelect(0, len(nums) - 1)