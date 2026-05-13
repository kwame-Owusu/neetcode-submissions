from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        look = defaultdict(list)

        for i in range(len(strs)):
            k = "".join(sorted(strs[i]))
            look[k].append(strs[i])
        
        return list(look.values())

