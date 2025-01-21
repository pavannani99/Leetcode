class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # n=len(gain)
        # self[n]={0}
        # self[0]=gain[0]
        #     for i in range(n):
        #         self[i]=self[i-1]-gain[i]
        #         gain.sort()
        # return gain[n-1]
        current_altitude = 0
        max_altitude = 0
        
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude
        