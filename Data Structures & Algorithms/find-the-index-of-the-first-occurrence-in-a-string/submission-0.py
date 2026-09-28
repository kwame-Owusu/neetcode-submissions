class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = -1

        for i in range(len(haystack)):
            j = i + len(needle)
            if haystack[i:j] == needle:
                idx = i
                break
        
        return idx