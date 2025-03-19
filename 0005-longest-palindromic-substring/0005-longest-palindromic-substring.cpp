class Solution {
public:
    string longestPalindrome(string s) {
        int start = 0, maxLength = 0;
        
        for (int i = 0; i < s.size(); i++) {
            for (int j = i; j < s.size(); j++) {
                if (isPalindrome(s, i, j) && (j - i + 1) > maxLength) {
                    start = i;
                    maxLength = j - i + 1;
                }
            }
        }
        
        return s.substr(start, maxLength);
    }
    
    bool isPalindrome(const string &s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++;
            right--;
        }
        return true;
    }
};
