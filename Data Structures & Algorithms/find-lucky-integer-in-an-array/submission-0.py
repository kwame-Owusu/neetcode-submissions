class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        count = Counter(arr)

        for key, val in count.items():
            if key == val:
                if key > res:
                    res = key
        
        return res