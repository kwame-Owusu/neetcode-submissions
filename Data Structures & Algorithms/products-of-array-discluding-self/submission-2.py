class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # first pass to build prefix, everything before index i
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # second pass to build suffix, everything after i
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for p, s in zip(prefix, suffix):
            res.append(p * s)
        
        return res
        

