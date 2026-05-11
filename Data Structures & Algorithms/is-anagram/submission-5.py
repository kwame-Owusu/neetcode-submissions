from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1
        

        for j in count_s:
            if count_s[j] != count_t[j]:
                return False
        
        return True
        
