from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        i = 0

        while i < k:
            # the key of the current max element
            curr_max = max(count, key=count.get)
            res.append(curr_max)
            del count[curr_max]
            i += 1
        
        return res




