class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index=m
        for i in range(n):
            nums1[index]=nums2[i]
            index=index+1
        return nums1.sort()
            
            
        