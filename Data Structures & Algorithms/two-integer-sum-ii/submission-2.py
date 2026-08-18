class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = [0] * 2
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                res[0] = l + 1
                res[1] = r + 1
                break
            elif currSum > target:
                r -= 1
            else:
                l += 1
        
        return res
