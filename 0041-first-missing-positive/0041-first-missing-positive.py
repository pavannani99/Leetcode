class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hey=1
        nums.sort()
        n=len(nums)
        for n in nums:
            if n==hey:
                hey+=1
            elif n>hey:
                return hey
        return hey