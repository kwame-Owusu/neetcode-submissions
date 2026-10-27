class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        count = Counter(nums)
        min_num = min(count) # minimum key 
        loop_range = (min_num + len(nums)) - 1

        for n in range(min_num, loop_range + 1):
            if count[n] != 1:
                return False
              
        return True
