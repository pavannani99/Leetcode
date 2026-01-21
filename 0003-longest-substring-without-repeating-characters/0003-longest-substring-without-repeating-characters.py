
"""


    l
     b
Input: s = " a b c a b c b b"
Output: 3
pseudo
base=0
longestsubstr=0
maxima=0
hasmap={}
while base <len(s):
    if element in haspmap:
    maxima=max(maxima,l-b)
    base=[hashmap[lookforward]]+1



"""




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        base=0
        lf=0
        hashmap={}
        maxima=0

        while lf<len(s):
            if s[lf] in hashmap and hashmap[s[lf]]>=base:
                maxima=max(maxima,lf-base)
                base=hashmap[s[lf]]+1
                hashmap[lf]=lf
                



            else:
                hashmap[s[lf]]=lf
            lf+=1
            maxima=max(maxima,lf-base)

        return maxima

        
        