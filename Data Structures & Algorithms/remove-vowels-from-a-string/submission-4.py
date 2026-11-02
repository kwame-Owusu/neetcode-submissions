class Solution:
    def removeVowels(self, s: str) -> str:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        res = []

        for char in s:
            if char not in vowel_set:
                res.append(char)

        return "".join(res)

