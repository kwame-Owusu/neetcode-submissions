class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = [0] * 2
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                res[0] = l + 1
                res[1] = r + 1
                break
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        
        return res