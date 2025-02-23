class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # if x < 0:
        #     return False
        
        
        # x_str = str(x)
        
        
        # return x_str == x_str[::-1]
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # Reverse half the digits
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even digit numbers: x == reversed_half
        # For odd digit numbers: x == reversed_half // 10 (middle digit is ignored)
        return x == reversed_half or x == reversed_half // 10

