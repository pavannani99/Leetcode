class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        
        if len(nums)<3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
        # nums=list(set(nums))
        # nums.sort(reverse=True)
        # if len(nums)>=3:
        #     return nums[2]
        # else:
        #     return nums[0]



        