class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':  # If string starts with '0', return 0
            return 0

        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_arr = [alpha[i] for i in range(26)]  # Storing 'a' to 'z' for reference (not used)
        
        set1 = []  # Used to store decoding possibilities (renamed from `set`)
        n = len(s)
        
        for i in range(n):
            set1.append(s[i])  # Store each character separately
        
        count = [0] * (n + 1)  # This will store decoding counts
        count[0], count[1] = 1, 1  # Base case: empty string and single digit
        
        for j in range(1, n):
            if '1' <= s[j] <= '9':  # Single-digit valid case
                count[j + 1] += count[j]
            
            two_digit = int(s[j - 1:j + 1])  # Two-digit number check
            if 10 <= two_digit <= 26:
                count[j + 1] += count[j - 1]
        
        return count[n]
