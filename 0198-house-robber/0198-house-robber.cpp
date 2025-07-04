class Solution {
public:
    int rob(vector<int>& nums) {
       
        int rob = 0, noRob = 0;
        for (int num : nums) {
            int newRob = noRob + num;
            noRob = max(rob, noRob);
            rob = newRob;
        }
        return max(rob, noRob);
   
    }
};