#include <vector>
#include <algorithm> // For std::sort

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        int index = m; // Starting index to append nums2 into nums1

        // Append nums2 elements into nums1 from index 'm'
        for (int j = 0; j < n; j++) {
            nums1[index] = nums2[j];
            index++;
        }

        // Sort nums1 after merging
        std::sort(nums1.begin(), nums1.end());
    }
};
