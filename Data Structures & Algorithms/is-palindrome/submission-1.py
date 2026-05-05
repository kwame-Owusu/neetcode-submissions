class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new string with only alphanumeric characters in lowercase
        result = []
        for char in s:
            if char.isalnum():
                result.append(char.lower())
        s = ''.join(result)

        # Initialize two pointers
        left = 0
        right = len(s) - 1

        # Check if the string is a palindrome
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        # solution without using the one line list comprehension
