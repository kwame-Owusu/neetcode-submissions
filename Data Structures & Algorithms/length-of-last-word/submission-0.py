class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        curr_word = ""

        for char in s:
            if char == " ":
                if curr_word.strip():
                    words.append(curr_word.strip())
                curr_word = ""
                continue
            curr_word += char
        
        if curr_word.strip():
            words.append(curr_word.strip()) 
        
        return len(words[-1])