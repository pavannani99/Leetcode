class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        i=0
        for i in range(n):
            if nums[i]==target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)