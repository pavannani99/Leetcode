class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr = 0;
int maxa = INT_MIN;  // need to declare the type
for(int num : nums) {  // need to specify type in C++
    curr = max(num, curr + num);
    maxa = max(maxa, curr);
}
return maxa;
    }
};