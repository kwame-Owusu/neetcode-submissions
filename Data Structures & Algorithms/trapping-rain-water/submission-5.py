class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            if max_l < max_r:
                l += 1
                water_amount = max_l - height[l]
                if water_amount > 0:
                    total += water_amount
                max_l = max(max_l, height[l])
            else:
                r -= 1
                water_amount = max_r - height[r]
                if water_amount > 0:
                    total += water_amount
                max_r = max(max_r, height[r])
        
        return total
