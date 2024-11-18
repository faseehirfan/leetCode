class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2

        l, r = 0, len(nums1) - 1

        while True: 
            mid_nums1 = l + (r-l) // 2
            mid_nums2 = half_len - mid_nums1 - 2

            left_nums1 = nums1[mid_nums1] if mid_nums1 >= 0 else float('-infinity')
            right_nums1 = nums1[mid_nums1 + 1] if mid_nums1 + 1 < len(nums1) else float('infinity')
            left_nums2 = nums2[mid_nums2] if  mid_nums2 >= 0 else float('-infinity')
            right_nums2 = nums2[mid_nums2 + 1] if mid_nums2 + 1 < len(nums2) else float('infinity')

            # valid partition
            if left_nums1 <= right_nums2 and left_nums2 <= right_nums1:
                if total_len % 2 == 1:
                    return min(right_nums1, right_nums2)
                else:
                    return (max(left_nums1, left_nums2) + min(right_nums1, right_nums2)) / 2
            
            elif left_nums1 > right_nums2:
                r = mid_nums1 - 1
            else:
                l = mid_nums1 + 1

