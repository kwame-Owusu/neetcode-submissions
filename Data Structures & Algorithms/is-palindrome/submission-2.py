class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new string with only alphanumeric characters in lowercase
        filtered_string = ""
        for char in s:
            if char.isalnum():
                filtered_string += char.lower()

        # Initialize two pointers
        left = 0
        right = len(filtered_string) - 1

        # Check if the string is a palindrome
        while left < right:
            if filtered_string[left] != filtered_string[right]:
                return False
            left += 1
            right -= 1
        return True
        # solution without using the one line list comprehension
