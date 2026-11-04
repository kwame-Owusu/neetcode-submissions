class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        window_set = set()

        for R in range(len(s)):
            while s[R] in window_set:
                window_set.remove(s[L])
                L += 1
            
            window_set.add(s[R])
            length = max(length, R - L + 1)
            
            
        return length