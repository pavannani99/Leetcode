class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()

        # Compare two possibilities:
        # 1. Product of the three largest numbers
        # 2. Product of two smallest numbers (negative) and the largest number
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
