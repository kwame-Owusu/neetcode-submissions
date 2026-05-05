class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    # this is the brute force solution using nested loop
                    # which has time Complexity of O(n^2)
