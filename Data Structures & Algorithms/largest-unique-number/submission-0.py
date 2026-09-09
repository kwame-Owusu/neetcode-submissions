class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        max_num = 0
        count = Counter(nums)

        for key, val in count.items():
            if key > max_num and val == 1:
                max_num = key
        
        return -1 if max_num == 0 else max_num