class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):  # Check all 32 bits
            if (n & (1 << i)) != 0:  # Check if the i-th bit is set
                res += 1
        return res
