class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
        
        # If we made it through all comparisons, it's a palindrome
        return True