class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        for i in range(len(nums) - 1):
            pair = (nums[i], nums[i + 1])
            if not ((pair[0] % 2 == 0 and pair[1] % 2 != 0) or (pair[0] % 2 != 0 and pair[1] % 2 == 0)):
                return False
        
        return True
