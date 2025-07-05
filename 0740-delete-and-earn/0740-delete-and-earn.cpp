class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        if(nums.empty()) return 0;
        
        map<int, int> count;
        for(int num : nums) {
            count[num] += num;
        }
        
        vector<int> keys;
        for(auto& p : count) {
            keys.push_back(p.first);
        }
        
        int n = keys.size();
        if(n == 1) return count[keys[0]];
        
        vector<int> dp(n);
        dp[0] = count[keys[0]];
        
        // Check if keys[1] is consecutive to keys[0]
        if(keys[1] == keys[0] + 1) {
            dp[1] = max(dp[0], count[keys[1]]);
        } else {
            dp[1] = dp[0] + count[keys[1]]; // Can take both!
        }
        
        for(int i = 2; i < n; i++) {
            if(keys[i] == keys[i-1] + 1) {
                // Consecutive: can't take both
                dp[i] = max(dp[i-1], dp[i-2] + count[keys[i]]);
            } else {
                // Not consecutive: can take both
                dp[i] = dp[i-1] + count[keys[i]];
            }
        }
        
        return dp[n-1];
    }
};