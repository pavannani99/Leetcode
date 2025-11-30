class Solution(object):
    def countSubstrings(self, s):
        res = 0
        
        for i in range(len(s)):
            
            res += self.palindrome(s, i, i)
           
            res += self.palindrome(s, i, i+1)
        
        return res

    def palindrome(self, s, l, r):
        res= 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
