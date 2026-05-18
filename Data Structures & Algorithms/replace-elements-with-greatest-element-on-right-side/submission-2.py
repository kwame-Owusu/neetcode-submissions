class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        right_max = -1
        
        # reverse iteration
        for i in range(len(arr) - 1, -1, -1):
            # new max = max(old_max, arr[i])
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        
        return arr
