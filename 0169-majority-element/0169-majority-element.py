class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
           # Initialize first element as candidate and count as 1
        candidate = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
            
            # If count drops to 0, pick a new candidate
            if count == 0:
                candidate = nums[i]
                count = 1
        
        return candidate       