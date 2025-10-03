class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        set_jw=set(jewels)
        cn=0
        for stone in stones:
            if stone in set_jw:
                cn+=1
        return cn


        