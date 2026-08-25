class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            count = 0
            # if count is more than 2 then we increase pointer
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
            
        return k
