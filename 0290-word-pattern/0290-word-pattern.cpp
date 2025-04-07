class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        string word = "";

        
        s += ' ';
        for (char c : s) {
            if (c == ' ') {
                words.push_back(word);
                word = "";
            } else {
                word += c;
            }
        }

        if (pattern.length() != words.size()) return false;

        // Your nested loop logic
        for (int i = 0; i < pattern.length(); i++) {
            for (int j = i + 1; j < pattern.length(); j++) {
                if ((pattern[i] == pattern[j] && words[i] != words[j]) ||
                    (pattern[i] != pattern[j] && words[i] == words[j])) {
                    return false;
                }
            }
        }

        return true;
    }
};
