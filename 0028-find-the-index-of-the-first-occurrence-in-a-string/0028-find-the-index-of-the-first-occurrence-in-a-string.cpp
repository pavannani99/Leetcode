class Solution {
public:
    int strStr(string haystack, string needle) {
        // Handle the case when needle is empty
        if (needle.empty()) {
            return 0;
        }

        // Ensure haystack is long enough to contain needle
        if (haystack.size() < needle.size()) {
            return -1;
        }

        // Traverse haystack while maintaining safe bounds
        for (int i = 0; i <= haystack.size() - needle.size(); i++) {
            bool match = true;

            // Check character-by-character for a match
            for (int j = 0; j < needle.size(); j++) {
                if (haystack[i + j] != needle[j]) {
                    match = false;
                    break;
                }
            }

            // If a full match is found, return the starting index
            if (match) {
                return i;
            }
        }

        // If no match is found, return -1
        return -1;
    }
};

