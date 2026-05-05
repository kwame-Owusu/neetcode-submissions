class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "{":"}","[":"]"}
        stack = []

        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if len(stack) == 0 or brackets[stack.pop()] != char:
                    return False
        return len(stack) == 0