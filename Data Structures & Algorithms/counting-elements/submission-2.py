from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = 0

        for key, val in count.items():
            if key + 1 in count.keys():
                res += val
        
        return res