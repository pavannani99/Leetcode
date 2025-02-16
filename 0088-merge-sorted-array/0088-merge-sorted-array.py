class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index=m
        for i in range(n):
            nums1[index]=nums2[i]
            index=index+1
        for j in range(len(nums1) - 1):
            for k in range(j + 1, len(nums1)):
                if nums1[j] > nums1[k]:
                    nums1[j], nums1[k] = nums1[k], nums1[j]  # Swap elements
        # middle=0
        # start=0
        # end=len(nums1)-1
        # while(start>end):
        #     if start>middle:
        #         nums1.swap(start,middle)
        #         middle+=1
        #     else if(end<middle):
        #         nums1.swap(middle,end)
        # else:
        #     return nums1    
            
            

            
            
        