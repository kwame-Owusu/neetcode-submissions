class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "{": "}", "[":"]"}
        stack = []

        for i in range(len(s)):
            if s[i] in brackets:
                stack.append(s[i])
            else:
                if not stack or brackets[stack.pop()] != s[i]:
                    return False
        
        return len(stack) == 0