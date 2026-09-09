class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []  # index mapping of nums1 to nums2

        hashmap = defaultdict(int)
        for i, n in enumerate(nums2):
            hashmap[n] = i

        for n in nums1:
            res.append(hashmap[n])
        
        return res