class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        counter = 0

        for i in range(len(nums)):
            if counter == 0 :
                candidate = nums[i]
            if nums[i] == candidate:
                counter += 1
            else:
                counter -= 1
        
        return candidate