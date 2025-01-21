class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # n=len(gain)
        # self[n]={0}
        # self[0]=gain[0]
        #     for i in range(n):
        #         self[i]=self[i-1]-gain[i]
        #         gain.sort()
        # return gain[n-1]
        a=0
        b=0
        for g in gain:
            a+=g
            b=max(b,a)
        return b
        