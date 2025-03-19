class Solution {
public:
    bool isPalindrome(string s) {
        string hey;
        for (char c : s) {
            if (isalnum(c)) { //nesure it is aplhabet or num
                hey.push_back(tolower(c));
            }
        }
        
        string rev = hey;
        reverse(rev.begin(), rev.end());
        
        return hey == rev;
    }
};
