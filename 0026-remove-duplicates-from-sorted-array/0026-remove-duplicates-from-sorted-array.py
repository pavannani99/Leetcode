class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums[:]=sorted(set(nums))
        # # return len(nums)
        if not  nums:
            return 0
        hey=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[hey]=nums[i]
                hey+=1
                
        return hey
        