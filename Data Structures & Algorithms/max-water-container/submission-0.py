class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            amount = width * height
            max_amount = max(max_amount, amount)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_amount
        

