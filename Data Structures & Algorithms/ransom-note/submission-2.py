class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_magazine = Counter(magazine)
        count_ransom = Counter(ransomNote)

        for key, val in count_ransom.items():
            if count_magazine[key] < val:
                return False
        
        return True