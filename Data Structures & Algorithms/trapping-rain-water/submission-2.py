class Solution:
    def trap(self, heights: List[int]) -> int:
        total = 0 # total amount of water
        l, r = 0, len(heights) - 1
        max_l, max_r = heights[l], heights[r]
        
        while l < r: 
            if max_l < max_r:
                l += 1
                water_amount = max_l - heights[l]
                if water_amount < 0:
                    water_amount = 0
                total += water_amount
                max_l = max(max_l, heights[l])
            else:
                r -= 1
                water_amount = max_r - heights[r]
                if water_amount < 0:
                    water_amount = 0
                total += water_amount
                max_r = max(max_r, heights[r])
                
        
        return total
            