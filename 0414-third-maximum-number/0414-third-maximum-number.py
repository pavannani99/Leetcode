class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        # n=len(nums)
        # if len(nums)<2:
        #     return nums[n-1]
        # else:
        #     return set(nums[n-3])
        nums=list(set(nums))
        nums.sort(reverse=True)
        if len(nums)>=3:
            return nums[2]
        else:
            return nums[0]


        