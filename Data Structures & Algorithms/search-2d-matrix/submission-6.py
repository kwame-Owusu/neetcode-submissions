class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1


        while l <= r:
            mid = l + (r - l) // 2

            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                search = self.binarySearch(matrix[mid], target)
                return search != -1
                
        return False

    
    def binarySearch(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1 # not found