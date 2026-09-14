class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = Counter(allowed)
        res = 0

        for word in words:
            all_chars_in_count = True
            for char in word:
                if char not in count:
                    all_chars_in_count = False
                    break
            
            if all_chars_in_count:
                res += 1
                    

        return res    