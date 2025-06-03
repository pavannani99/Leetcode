class Solution:
    def isPalindrome(self, s: str) -> bool:
         hey = ''.join(ch.lower() for ch in s if ch.isalnum())
         return hey == hey[::-1]   

        