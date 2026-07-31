class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)


        # build prefix list, every element before i
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # build suffix list, every element after i
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for p, s in zip(prefix, suffix):
            res.append(p * s)
        
        return res
        
        