class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False
        num_set=set()
        # for n in nums:
        #     if n in num_set:
        #         return True
        #     num_set.add(n)
        # return False
        return True if len(set(nums))<len(nums) else  False