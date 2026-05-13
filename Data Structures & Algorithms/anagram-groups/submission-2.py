from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        look = defaultdict(list)
        res = []

        for i in range(len(strs)):
            k = "".join(sorted(strs[i]))
            look[k].append(strs[i])
        
        for key, val in look.items():
            res.append(val)
            
        return res

