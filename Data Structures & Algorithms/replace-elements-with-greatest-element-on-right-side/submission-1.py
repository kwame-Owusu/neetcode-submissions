class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i + 1 :])
        
        arr[-1] = -1

        return arr #O(n^2) because of max() having to compare with all other elements again