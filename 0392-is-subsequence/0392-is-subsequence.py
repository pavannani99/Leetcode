class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        # Iterate through 't' to check for subsequence
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move in 's' if match found
            j += 1  # Always move in 't'

        # If i reached the end of 's', it's a subsequence
        if i==len(s):
            return True
        return False