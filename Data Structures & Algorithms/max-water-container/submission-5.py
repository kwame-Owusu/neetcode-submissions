class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            curr_amount = width * height # area
            max_amount = max(max_amount, curr_amount)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_amount