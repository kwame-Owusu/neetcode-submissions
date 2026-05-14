from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        maxCount = 0

        for key, val in count.items():
            if maxCount < val:
                res = key
                maxCount = val
        
        return res