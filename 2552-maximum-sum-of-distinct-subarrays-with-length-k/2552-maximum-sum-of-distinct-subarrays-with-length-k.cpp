class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        unordered_set<int> s;
        long long sum = 0, maxSum = 0;
        int n = nums.size();

        for (int i = 0, j = 0; j < n; j++) {
            
            while (s.count(nums[j])) {
                s.erase(nums[i]);
                sum -= nums[i];
                i++;
            }

            s.insert(nums[j]);
            sum += nums[j];

            
            if (j - i + 1 == k) {
                maxSum = max(maxSum, sum);

               
                s.erase(nums[i]);
                sum -= nums[i];
                i++;
            }
        }

        return maxSum;
    }
};
