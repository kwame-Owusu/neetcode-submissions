class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        total_sum = 0

        for num in nums:
            total_sum += num
            max_sum = max(max_sum, total_sum)
            if total_sum < 0:
                total_sum = 0

        return max_sum