class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        # Check if n is a power of two
        if n & (n - 1) == 0:
            # Check if n is a power of four (1-bit at even position)
            return (n - 1) % 3 == 0
        return False
