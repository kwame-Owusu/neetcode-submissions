class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sublist = []

        def backtrack(i, sublist):
            if i >= len(nums):
                res.append(sublist[:])
                return
            
            # include nums[i]
            sublist.append(nums[i])
            backtrack(i+1, sublist)
            
            # exclude nums[i]
            sublist.pop()
            backtrack(i+1, sublist)
        
        backtrack(0, sublist)
        return res
        
        
            

            
