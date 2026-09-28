class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # monotonic increasing stack of pairs (index, height)
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                popped_idx, popped_height = stack.pop()
                curr_area = popped_height * (i - popped_idx)
                max_area = max(max_area, curr_area)
                start = popped_idx
            stack.append((start, height))

        for idx, height in stack:
            # Bars left in the stack extend to the end of the array
            area = height * (len(heights) - idx)
            max_area = max(max_area, area)
        
        return max_area
