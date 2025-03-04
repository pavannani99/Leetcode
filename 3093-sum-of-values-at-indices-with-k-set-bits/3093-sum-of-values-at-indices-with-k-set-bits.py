class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        x=0
        for i in range(len(nums)):
            b=bin(i)[2:]
            count=0
            for j in b:
                if j=='1':
                    count+=1
            if count==k:
                 x=x+nums[i]
        return x
        