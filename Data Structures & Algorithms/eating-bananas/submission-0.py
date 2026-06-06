class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = 0
        
        
        while low <= high:
            mid = low + ( high - low ) // 2 # candidate speed k
            totalTime = 0
            for p in piles:
                totalTime += (p + mid - 1) // mid
            
            if totalTime <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
            



