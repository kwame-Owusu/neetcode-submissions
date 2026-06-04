class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                search = self.binarySearch(matrix[mid], target)
                return search != -1

        return False

    def binarySearch(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + (R - L) // 2  # prevent interger overflow

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return -1
