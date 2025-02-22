class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        hey=[]
        n = len(nums)
        k = k % n 
        if n <= 1 or k == 0:
            return
         # In case k > n
        
        # Store last k elements in 'hey'
        hey = nums[-k:]
        
        # Remove last k elements and place them at the front
        nums[:] = hey + nums[:n - k]
            
       
            

        
            

        """
        Do not return anything, modify nums in-place instead.
        """