class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums1) # mapping indices

        hashmap = defaultdict(int) # holding the indices of nums2
        for i, n in enumerate(nums2):
            hashmap[n] = i
        
        for i, n in enumerate(nums1):
            res[i] = hashmap[n]
        
        return res
            