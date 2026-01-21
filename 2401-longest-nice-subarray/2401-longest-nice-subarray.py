class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left=0
        mask=0
        max_len=0
        for right in range(len(nums)):
            while mask & nums[right] != 0:
                mask=mask^nums[left]
                left+=1
            mask |= nums[right] 
            max_len = max(max_len, right - left + 1)
        return max_len
            
        