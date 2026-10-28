class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        nums.extend(nums1)
        nums.extend(nums2)
        nums.sort()
        # space = O(n + m)
        res = 0
        n = len(nums)
        if len(nums) % 2 != 0:
            res = nums[n // 2]
        else:
            first = nums[(n // 2) - 1]  # The left-middle element
            second = nums[n // 2]       # The right-middle element
            res = (first + second) / 2
        # time complexity = o(n log n)
        return res