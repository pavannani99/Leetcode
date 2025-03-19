#include <iostream>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int cnt = 0;
        unordered_set<char> hey;
        int left = 0;
        
        for (int i = 0; i < s.size(); i++) {
            // If the character is already in the set, adjust the window
            while (hey.find(s[i]) != hey.end()) {
                hey.erase(s[left]);
                left++;
            }
            // Insert current character and update count
            hey.insert(s[i]);
            cnt = max(cnt, i - left + 1);
        }
        
        return cnt;
    }
};

