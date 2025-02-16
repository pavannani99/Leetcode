class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2,p=m-1,n-1,m+n-1

        while p1>=0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[p]=nums1[p1]
                p1-=1

            else:
                nums1[p]=nums2[p2]
                p2-=1
            p-=1
          # If any elements are left in nums2, copy them (nums1 elements are already in place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        # index=m
        # for i in range(n):
        #     nums1[index]=nums2[i]
        #     index=index+1
        # for j in range(len(nums1) - 1):
        #     for k in range(j + 1, len(nums1)):
        #         if nums1[j] > nums1[k]:
        #             nums1[j], nums1[k] = nums1[k], nums1[j]  # Swap elements
        # # middle=0
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
            
            

            
            
        