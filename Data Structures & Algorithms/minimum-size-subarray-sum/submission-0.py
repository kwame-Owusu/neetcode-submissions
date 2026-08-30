class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float("inf")


        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res) # current elements in window
                total -= nums[l] # subtract l from the total as we are leaving it behind
                l += 1
        
        return 0 if res == float("inf") else res

