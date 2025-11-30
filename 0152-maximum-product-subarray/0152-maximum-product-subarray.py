class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=max(nums)
        cmin,cmax=1,1
        for n in nums:
            if n==0:
                cmin,cmax=1,1
                continue
            
            temp = cmax * n
            cmax = max(n * cmax, n * cmin, n)
            cmin = min(temp, n * cmin, n)

            res = max(res, cmax)
        return res

        