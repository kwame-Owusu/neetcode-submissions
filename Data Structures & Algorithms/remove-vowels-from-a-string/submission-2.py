class Solution:
    def removeVowels(self, s: str) -> str:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        word_list = list(s)
        res = ""

        for i in range(len(word_list)):
            if word_list[i] not in vowel_set:
                res += word_list[i]   
            continue        

        return res

