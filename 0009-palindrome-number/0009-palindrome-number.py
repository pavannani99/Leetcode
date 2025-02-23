class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers can't be palindromes due to the '-' sign
        if x < 0:
            return False
        
        # Convert the integer to string
        x_str = str(x)
        
        # Check if the string is the same when reversed
        return x_str == x_str[::-1]
