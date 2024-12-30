class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res; // To store the result
        int n = nums.size();
        
        // Step 1: Sort the array
        sort(nums.begin(), nums.end());
        
        // Step 2: Four nested loops
        for (int i = 0; i < n - 3; i++) {
            // Skip duplicates for the first pointer
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < n - 2; j++) {
                // Skip duplicates for the second pointer
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                for (int k = j + 1; k < n - 1; k++) {
                    // Skip duplicates for the third pointer
                    if (k > j + 1 && nums[k] == nums[k - 1]) continue;

                    for (int l = k + 1; l < n; l++) {
                        // Skip duplicates for the fourth pointer
                        if (l > k + 1 && nums[l] == nums[l - 1]) continue;

                        // Check if the sum matches the target
                        if ((long long)nums[i] + nums[j] + nums[k] + nums[l] == target) {
                            res.push_back({nums[i], nums[j], nums[k], nums[l]});
                        }
                    }
                }
            }
        }

        return res;
    }
};
