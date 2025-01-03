class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
        
        #for i in range(n-k-1,-1,-1):
         # //  if nums[i]!=nums[i+1]:
          #  //    print(nums[i])
           #   //  break
