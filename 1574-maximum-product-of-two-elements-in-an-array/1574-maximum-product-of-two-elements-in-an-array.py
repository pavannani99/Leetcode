class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # hey=0
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         ctr =abs(nums[i]-1) * (nums[j]-1)
        #         hey=max(ctr,hey)
        # return hey
        first = second = 0
        for num in nums:
            if num > first:
                first, second = num, first
            elif num > second:
                second = num
        return (first - 1) * (second - 1)
