class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, length = 0, 0 
        window_set = set()

        for R in range(len(s)):
            while s[R] in window_set:
                window_set.remove(s[L])
                L += 1


            length = max(R - L + 1, length)
            window_set.add(s[R])
        
        return length
        

