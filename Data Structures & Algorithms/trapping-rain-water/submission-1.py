class Solution:
    def trap(self, heights: List[int]) -> int:
        total = 0 # total amount of water
        l, r = 0, len(heights) - 1
        max_l, max_r = heights[l], heights[r]
        
        while l < r: 
            if max_l < max_r:
                l += 1
                max_l = max(max_l, heights[l])
                total += max_l - heights[l]
            else:
                r -= 1
                max_r = max(max_r, heights[r])
                total += max_r - heights[r]
                
        
        return total
            