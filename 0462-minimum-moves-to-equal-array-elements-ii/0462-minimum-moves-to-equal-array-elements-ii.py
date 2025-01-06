class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()  # Sort the array
        median = nums[len(nums) // 2]  # Find the median
        return sum(abs(num - median) for num in nums)  # Calculate total moves
