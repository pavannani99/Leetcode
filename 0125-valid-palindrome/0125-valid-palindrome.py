class Solution:
    def isPalindrome(self, s: str) -> bool:
        hey=[]
        for i in s:
            if i.isalnum():

                   hey.append(i.lower())
        hello=hey[::-1]
        if hey==hello:
            return True
        return False

        