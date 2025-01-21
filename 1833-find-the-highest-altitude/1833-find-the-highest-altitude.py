class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        a=0
        b=0
        for g in gain:
            a+=g
            b=max(b,a)
        return b
        

        # dry run
        # -5,1,5,0,-7
        # g=-5   a=g  max(0,-5)==0
        # g=-5+1  a=-4  max(0,-4)==0
        # g=-4+5  a=1    max(0,1)==1
        # g=0 max(1,1)==1
        # # g=1-7  a=-6 max(1,-6)==1